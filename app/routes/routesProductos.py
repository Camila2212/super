from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.routes.routesCarrito import carrito_compras
from app.models.Producto import Producto
from flask_login import current_user,login_required
from app import db
import os

bp = Blueprint('producto', __name__)

@bp.route('/Producto')
def index():
    data = Producto.query.all()
    
    return render_template('app/productos.html', data=data, t=carrito_compras.tamañoD())
    #return render_template('producto/index.html', data=data, t=carrito_compras.tamañoD())


@bp.route('/Producto/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        img = request.files['img']
        
        guardarImg(img)

        new_producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, cantidad=cantidad, img=img.filename)
        db.session.add(new_producto)
        db.session.commit()
        
        return render_template('app/productos.html')
        # return redirect(url_for('producto.index'))

    return render_template('producto/add.html')

@bp.route('/Producto/edit/<int:idProd>', methods=['GET', 'POST'])
def edit(idProd):
    producto = Producto.query.get_or_404(idProd)

    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descripcion']
        producto.precio = request.form['precio']
        producto.cantidad = request.form['cantidad']


        db.session.commit()
        return redirect(url_for('producto.index'))

    return render_template('producto/edit.html', producto=producto)
    

@bp.route('/Producto/delete/<int:idProd>')
def delete(idProd):
    producto = Producto.query.get_or_404(idProd)
    
    db.session.delete(producto)
    db.session.commit()

    return redirect(url_for('producto.index'))


 
@bp.route('/Productos')
def index1():
    data = Producto.query.all()
    
    return render_template('producto/index.html', data=data)

def guardarImg(img):
    from run import app
    carpetaDestino = os.path.join(app.root_path,"static","img")
    img.save(os.path.join(carpetaDestino, img.filename))


@bp.route('/filtrar/<tipo>')
def filtrar_productos(tipo):
    # Asume que 'data' es una lista de productos
    resultados = Producto.query.filter_by(descripcion=tipo).all()
    data = Producto.query.all()
    # productos_filtrados = [producto for producto in data if tipo in producto['descripcion'].lower()]
    return render_template('app/productos.html', data=data, resultados=resultados, t=carrito_compras.tamañoD())