from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.Producto import Producto
from app.models.Carrito import Carrito
from app.models.FacturaVenta import FacturaVenta
from app.models.DetalleVenta import DetalleVenta
from flask_login import current_user,login_required
from app import db

bp = Blueprint('carritos', __name__)
carrito_compras = Carrito()

@bp.route('/ListarCarritooo')
@login_required
def listar():
    total = carrito_compras.calcular_total()
    items = carrito_compras.getItems()
    return render_template('producto/List.html', items=items, total=total)



@bp.route('/ListarProductos')
@login_required
def index():
    productos = carrito_compras
    total = sum(item['producto'].precio * item['cantidad'] for item in carrito_compras)
    return render_template('index.html', Producto=productos, items=carrito_compras, total=total)


@bp.route('/agregar/<int:id>', methods=['POST'])
@login_required
def agregar_al_carrito(id):



    cantidad = int(request.form.get('cantidad', 1))

    noprod = Producto.query.get_or_404(id)
    if not noprod.cantidad>cantidad:
        return redirect(url_for('producto.index'))

    items = carrito_compras.getItems()
    for item in items:
        if item['producto'].idProd == id:
            item['cantidad'] += cantidad
            return redirect(url_for('producto.index'))
    carrito_compras.agregar_producto(id, cantidad)
    return redirect(url_for('producto.index'))

@bp.route('/eliminar/<int:id>', methods=['POST','GET'])
@login_required
def eliminaritem(id):
    items = carrito_compras.getItems()
    for item in items:
        if item['producto'].idProd == id:
            carrito_compras.eliminarItem(item)
            return redirect(url_for('carritos.listar'))  # Redirigir a la vista del carrito
    return redirect(url_for('carritos.listar'))  # Redirigir a la vista del carrito

@bp.route('/realizar_compra')
@login_required
def realizar_compra():
    


    total = carrito_compras.calcular_total()

    factura = FacturaVenta(dtoFV=1, totalFV= total, idAdmin=1, idCliente=current_user.idCliente)
    db.session.add(factura)
    db.session.commit()

    productos = carrito_compras.getItems()

    for producto in productos:
        pd=producto["producto"]
        newDetalleVenta=DetalleVenta(cantidadDV=producto["cantidad"], subTotalDV=pd.precio, idProd=pd.idProd, idFV=factura.idFV)
        cantidad=Producto.query.get_or_404(pd.idProd)
        cantidad.cantidad -= producto["cantidad"]
        db.session.add(newDetalleVenta)

    db.session.commit()


    detallesVenta = DetalleVenta.query.filter_by(idFV=factura.idFV) 


    total = carrito_compras.calcular_total()


    
    # Aquí puedes almacenar la información en la base de datos (crear registros en Carrito y Factura)
    # y luego limpiar el carrito de compras
    carrito_compras.carrito = []

    carrito_compras.vaciarcarrito()
    return render_template("facturaVenta/index.html", miFactura=factura, detallesVenta=detallesVenta, total=total)




    return render_template('carrito/realizar_compra.html', total=total)

@bp.route('/generar_factura', methods=['POST'])
def generar_factura():
    total = carrito_compras.calcular_total()

    
    # Aquí puedes almacenar la información en la base de datos (crear registros en Carrito y Factura)
    # y luego limpiar el carrito de compras
    carrito_compras.carrito = []
    return render_template('carrito/factura.html', total=total)



@bp.route('/itemscarrito', methods=['GET', 'POST'])
@login_required
def tCarrito():
    a = carrito_compras.tamañoD()
    print("Entra a carrito rutas", a)
    return f"Entra a carrito {carrito_compras.tamañoD()}"


@bp.route('/vaciar_carrito', methods=['POST'])
@login_required
def vaciar_carrito():
    carrito_compras.vaciarcarrito()
    return render_template('producto/List.html')

