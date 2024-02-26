from app import db

class Producto(db.Model):
    idProd = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable=True)
    img = db.Column(db.String(255), nullable=True)
    facturaVenta = db.relationship("FacturaVenta", secondary="detalle_venta", back_populates="producto")
