from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.FacturaVenta import FacturaVenta
from app.models.Administrador import Administrador
from app.models.Cliente import Cliente
from app import db

bp = Blueprint('facturaVenta', __name__)


@bp.route('/FacturaVenta1')
def index1():
    data = FacturaVenta.query.all()
    
    return render_template('facturaVenta/index1.html', data=data)

@bp.route('/FacturaVenta')
def index():
    data = FacturaVenta.query.all()
    
    return render_template('facturaVenta/index.html', data=data)

@bp.route('/FacturaVenta/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        dtoFV = request.form['dtoFV']
        
        totalFV = request.form['totalFV']
        idAdmin = request.form['idAdmin']
        idCliente = request.form['idCliente']
            
        
        new_facturaVenta = FacturaVenta (dtoFV=dtoFV, totalFV=totalFV, idAdmin=idAdmin, idCliente=idCliente)
        db.session.add(new_facturaVenta)
        db.session.commit()
        
        return redirect(url_for('facturaVenta.index'))
    
    data = Administrador.query.all()
    cliente = Cliente.query.all()
    return render_template('facturaVenta/add.html', data=data, cliente=cliente)

@bp.route('/FacturaVenta/edit/<int:idFV>', methods=['GET', 'POST'])
def edit(idFV):
    facturaVenta = FacturaVenta.query.get_or_404(idFV)

    if request.method == 'POST':
        facturaVenta.dtoFV = request.form['dtoFV']
        facturaVenta.fechaFV = request.form['fechaFV']
        facturaVenta.totalFV = request.form['totalFV']
        facturaVenta.idAdmin = request.form['idAdmin']
        facturaVenta.idCliente = request.form['idCliente']


        db.session.commit()
        return redirect(url_for('facturaVenta.index'))

    return render_template('facturaVenta/edit.html', facturaVenta=facturaVenta)
    

@bp.route('/FacturaVenta/delete/<int:idFV>')
def delete(idFV):
    facturaVenta = FacturaVenta.query.get_or_404(idFV)
    
    db.session.delete(facturaVenta)
    db.session.commit()

    return redirect(url_for('facturaVenta.index'))
