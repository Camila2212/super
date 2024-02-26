from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.FacturaCompra import FacturaCompra
from app.models.Administrador import Administrador
from app.models.Proveedor import Proveedor


from app import db

bp = Blueprint('facturaCompra', __name__)

@bp.route('/FacturaCompra')
def index():
    data = FacturaCompra.query.all()
    
    return render_template('facturaCompra/index.html', data=data)

@bp.route('/FacturaCompra/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        dtoFC = request.form['dtoFC']

        totalFC = request.form['totalFC']
        idAdmin = request.form['idAdmin']
        idProv = request.form['idProv']
            
        
        new_facturaCompra = FacturaCompra (dtoFC=dtoFC, totalFC=totalFC, idAdmin=idAdmin, idProv=idProv)
        db.session.add(new_facturaCompra)
        db.session.commit()
        
        return redirect(url_for('facturaCompra.index'))

    data = Administrador.query.all()
    proveedor = Proveedor.query.all()
    return render_template('facturaCompra/add.html', data=data, proveedor=proveedor)

@bp.route('/FacturaCompra/edit/<int:idFC>', methods=['GET', 'POST'])
def edit(idFC):
    facturaCompra = FacturaCompra.query.get_or_404(idFC)

    if request.method == 'POST':
        facturaCompra.dtoFC = request.form['dtoFC']
        facturaCompra.fechaFC = request.form['fechaFC']
        facturaCompra.totalFC = request.form['totalFC']
        facturaCompra.idAdmin = request.form['idAdmin']
        facturaCompra.idProv = request.form['idProv']


        db.session.commit()
        return redirect(url_for('facturaCompra.index'))

    return render_template('facturaCompra/edit.html', facturaCompra=facturaCompra)
    

@bp.route('/FacturaCompra/delete/<int:idFC>')
def delete(idFC):
    facturaCompra = FacturaCompra.query.get_or_404(idFC)
    
    db.session.delete(facturaCompra)
    db.session.commit()

    return redirect(url_for('facturaCompra.index'))
