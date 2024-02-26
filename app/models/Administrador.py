from flask_login import UserMixin
from app import db

class Administrador(db.Model, UserMixin):
    idAdmin = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    cedula = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    clave = db.Column(db.String(255), nullable=False)

    def get_id(self):
        return str(self.idAdmin)