from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import func



class FacturaVenta(db.Model):
    idFV = db.Column(db.Integer, primary_key=True)
    dtoFV = db.Column(db.Integer, nullable=False)
    fechaFV = db.Column(db.Date, nullable=False, default=func.now())
    totalFV = db.Column(db.Integer, nullable=False)
    idAdmin = db.Column(db.Integer, db.ForeignKey('administrador.idAdmin'))
    idCliente = db.Column(db.Integer, db.ForeignKey('cliente.idCliente'))
    cliente = db.relationship("Cliente", back_populates="facturaVenta")
    producto = db.relationship("Producto", secondary="detalle_venta", back_populates="facturaVenta")