from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Administrador import Administrador
from app import db

bp = Blueprint('administrador', __name__)

@bp.route('/Administrador')

def index():
    data = Administrador.query.all()
    
    return render_template('administrador/index.html', data=data)

@bp.route('/Administrador/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        cedula = request.form['cedula']
        telefono = request.form['telefono']
        correo = request.form['correo']
        direccion = request.form['direccion']
        clave = request.form['clave']
        
        new_administrador = Administrador(nombre=nombre, apellido=apellido, cedula=cedula, telefono=telefono, correo=correo, direccion=direccion, clave=clave)
        db.session.add(new_administrador)
        db.session.commit()

        return redirect(url_for('administrador.index'))

    return render_template('administrador/add.html')

@bp.route('/Administrador/edit/<int:idAdmin>', methods=['GET', 'POST'])
def edit(idAdmin):
    administrador = Administrador.query.get_or_404(idAdmin)

    if request.method == 'POST':
        administrador.nombre = request.form['nombre']
        administrador.apellido = request.form['apellido']
        administrador.cedula = request.form['cedula']
        administrador.telefono = request.form['telefono']
        administrador.correo = request.form['correo']
        administrador.direccion = request.form['direccion']
        administrador.contrasena = request.form['contrasena']

        db.session.commit()
        return redirect(url_for('administrador.index'))

    return render_template('administrador/edit.html', administrador=administrador)
    

@bp.route('/Administrador/delete/<int:idAdmin>')
def delete(idAdmin):
    administrador = Administrador.query.get_or_404(idAdmin)
    
    db.session.delete(administrador)
    db.session.commit()

    return redirect(url_for('administrador.index'))
