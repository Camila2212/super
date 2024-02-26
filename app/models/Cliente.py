from flask_login import UserMixin
from app import db

class Cliente(db.Model, UserMixin):
    idCliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    cedula = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    clave = db.Column(db.String(255), nullable=False)
    facturaVenta = db.relationship("FacturaVenta", back_populates="cliente")
    def get_id(self):
        return str(self.idCliente)
