from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Proveedor import Proveedor
from app import db

bp = Blueprint('proveedor', __name__)

@bp.route('/Proveedor')
def index():
    data = Proveedor.query.all()
    
    return render_template('proveedor/index.html', data=data)

@bp.route('/Proveedor/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nit = request.form['nit']
        telefono = request.form['telefono']
        correo = request.form['correo']
            
        
        new_proveedor = Proveedor(nombre=nombre, nit=nit, telefono=telefono, correo=correo)
        db.session.add(new_proveedor)
        db.session.commit()
        
        return redirect(url_for('proveedor.index'))

    return render_template('proveedor/add.html')

@bp.route('/Proveedor/edit/<int:idProv>', methods=['GET', 'POST'])
def edit(idProv):
    proveedor = Proveedor.query.get_or_404(idProv)

    if request.method == 'POST':
        proveedor.nombre = request.form['nombre']
        proveedor.nit = request.form['nit']
        proveedor.telefono = request.form['telefono']
        proveedor.correo = request.form['correo']


        db.session.commit()
        return redirect(url_for('proveedor.index'))

    return render_template('proveedor/edit.html', proveedor=proveedor)
    

@bp.route('/Proveedor/delete/<int:idProv>')
def delete(idProv):
    proveedor = Proveedor.query.get_or_404(idProv)
    
    db.session.delete(proveedor)
    db.session.commit()

    return redirect(url_for('proveedor.index'))
