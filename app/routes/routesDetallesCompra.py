from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.DetalleCompra import DetalleCompra
from app.models.Producto import Producto
from app.models.FacturaCompra import FacturaCompra

from app import db

bp = Blueprint('detalleCompra', __name__)

@bp.route('/DetalleCompra')
def index():
    data = DetalleCompra.query.all()
    
    return render_template('detalleCompra/index.html', data=data)

@bp.route('/DetalleCompra/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        cantidadDC = request.form['cantidadDC']
        subTotalDC = request.form['subTotalDC']
        idProd = request.form['idProd']
        idFC = request.form['idFC']
            
        
        new_detalleCompra = DetalleCompra (cantidadDC=cantidadDC, subTotalDC=subTotalDC, idProd=idProd, idFC=idFC)
        db.session.add(new_detalleCompra)
        db.session.commit()
        
        return redirect(url_for('detalleCompra.index'))
    data = Producto.query.all()
    facturaCompra = FacturaCompra.query.all()
    return render_template('detalleCompra/add.html', data=data, facturaCompra=facturaCompra)

@bp.route('/DetalleCompra/edit/<int:idDC>', methods=['GET', 'POST'])
def edit(idDC):
    detalleCompra = DetalleCompra.query.get_or_404(idDC)

    if request.method == 'POST':
        detalleCompra.cantidadDC = request.form['cantidadDC']
        detalleCompra.subTotalDC = request.form['subTotalDC']
        detalleCompra.idProd = request.form['idProd']
        detalleCompra.idFC = request.form['idFC']


        db.session.commit()
        return redirect(url_for('detalleCompra.index'))
      
    return render_template('detalleCompra/edit.html', detalleCompra=detalleCompra)
    

@bp.route('/DetalleCompra/delete/<int:idDC>')
def delete(idDC):
    detalleCompra = DetalleCompra.query.get_or_404(idDC)
    
    db.session.delete(detalleCompra)
    db.session.commit()

    return redirect(url_for('detalleCompra.index'))
