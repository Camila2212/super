from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.DetalleVenta import DetalleVenta
from app.models.Producto import Producto
from app.models.FacturaVenta import FacturaVenta
from app.routes.routesCarrito import carrito_compras
from app import db

bp = Blueprint('detalleVenta', __name__)

@bp.route('/DetalleVenta')
def index():
    data = DetalleVenta.query.all()
    
    return render_template('detalleVenta/index.html', data=data)

@bp.route('/DetalleVenta/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        cantidadDV = request.form['cantidadDV']
        subTotalDV = request.form['subTotalDV']
        idProd = request.form['idProd']
        idFV = request.form['idFV']
            
        
        new_detalleVenta = DetalleVenta (cantidadDV=cantidadDV, subTotalDV=subTotalDV, idProd=idProd, idFV=idFV)
        db.session.add(new_detalleVenta)
        db.session.commit()
        
        return redirect(url_for('detalleVenta.index'))
    data = Producto.query.all()
    facturaVenta = FacturaVenta.query.all()

    return render_template('detalleVenta/add.html', data=data, facturaVenta=facturaVenta)



@bp.route('/adddetalle/<int:id>', methods=['GET', 'POST'])  
def addDetalle(id):  
    for item in carrito_compras.getItems():
        idprod = item["producto"].idprod      
        detalleVenta = DetalleVenta(idFV=id,idprod=idprod)
        db.session.add(detalleVenta)
        db.session.commit() 
    carrito_compras.vaciarcarrito()
    return redirect(url_for('producto.index'))

@bp.route('/DetalleVenta/edit/<int:idDV>', methods=['GET', 'POST'])
def edit(idDV):
    detalleVenta = DetalleVenta.query.get_or_404(idDV)

    if request.method == 'POST':
        detalleVenta.cantidadDV = request.form['cantidadDV']
        detalleVenta.subTotalDV = request.form['subTotalDV']
        detalleVenta.idProd = request.form['idProd']
        detalleVenta.idFV = request.form['idFV']


        db.session.commit()
        return redirect(url_for('detalleVenta.index'))

    return render_template('detalleVenta/edit.html', detalleVenta=detalleVenta)
    

@bp.route('/DetalleVenta/delete/<int:idDV>')
def delete(idDV):
    detalleVenta = DetalleVenta.query.get_or_404(idDV)
    
    db.session.delete(detalleVenta)
    db.session.commit()

    return redirect(url_for('detalleVenta.index'))
