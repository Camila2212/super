from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Cliente import Cliente
from app import db

bp = Blueprint('cliente', __name__)

@bp.route('/Cliente')
def index():
    data = Cliente.query.all()
    
    return render_template('cliente/index.html', data=data)

@bp.route('/Cliente/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        cedula = request.form['cedula']
        telefono = request.form['telefono']
        correo = request.form['correo']
        direccion = request.form['direccion']
        clave = request.form['clave1']

        
        
        new_cliente = Cliente(nombre=nombre, apellido=apellido, cedula=cedula, telefono=telefono, correo=correo, direccion=direccion, clave=clave)
        db.session.add(new_cliente)
        db.session.commit()
        
        return render_template('app/publico.html')


    return render_template('cliente/add.html')

@bp.route('/Cliente/edit/<int:idCliente>', methods=['GET', 'POST'])
def edit(idCliente):
    cliente = Cliente.query.get_or_404(idCliente)

    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.apellido = request.form['apellido']
        cliente.cedula = request.form['cedula']
        cliente.telefono = request.form['telefono']
        cliente.correo = request.form['correo']
        cliente.direccion = request.form['direccion']
        cliente.clave = request.form['clave1']


        db.session.commit()
        return redirect(url_for('cliente.index'))

    return render_template('cliente/edit.html', cliente=cliente)
    

@bp.route('/Cliente/delete/<int:idCliente>')
def delete(idCliente):
    cliente = Cliente.query.get_or_404(idCliente)
    
    db.session.delete(cliente)
    db.session.commit()

    return redirect(url_for('cliente.index'))
