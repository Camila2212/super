from app import db
from sqlalchemy.orm import relationship

class DetalleCompra(db.Model):
    idDC = db.Column(db.Integer, primary_key=True)
    cantidadDC = db.Column(db.Integer,  nullable=False)
    subTotalDC = db.Column(db.Integer,  nullable=False)
    idProd = db.Column(db.Integer, db.ForeignKey('producto.idProd'))
    idFC = db.Column(db.Integer, db.ForeignKey('factura_compra.idFC'))
    