from app import db
from sqlalchemy.orm import relationship

class DetalleVenta(db.Model):
    idDV = db.Column(db.Integer, primary_key=True)
    cantidadDV = db.Column(db.Integer,  nullable=False)
    subTotalDV = db.Column(db.Integer,  nullable=False)
    idProd = db.Column(db.Integer, db.ForeignKey('producto.idProd'))
    idFV = db.Column(db.Integer, db.ForeignKey('factura_venta.idFV'))
    producto = db.relationship("Producto")