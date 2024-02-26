from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.Administrador import Administrador
from app.models.Cliente import Cliente


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        clave = request.form['clave']
        
        cliente = Cliente.query.filter_by(correo=correo, clave=clave).first()

        if cliente:
            login_user(cliente)
          
            return render_template("app/publico.html")
       
    
        administrador = Administrador.query.filter_by(correo=correo, clave=clave).first()

        if administrador:
            login_user(administrador)
            flash("Login successful!", "success")
            return render_template("app/privado.html")

        flash('Invalid credentials. Please try again.', 'danger')
    
    return render_template("login/login.html")


@auth_bp.route('/miInicio')
@login_required
def miInicio():
    return render_template("app/publico.html")



@auth_bp.route('/dashboard')
@login_required
def dashboard():
    return f'Welcome, {current_user.correo}! This is your dashboard.'

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
   