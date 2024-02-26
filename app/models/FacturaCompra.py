from app import db
from sqlalchemy.orm import relationship


class FacturaCompra(db.Model):
    idFC = db.Column(db.Integer, primary_key=True)
    dtoFC = db.Column(db.Integer, nullable=False)
    fechaFC = db.Column(db.Date, nullable=False)
    totalFC = db.Column(db.Integer, nullable=False)
    idAdmin = db.Column(db.Integer, db.ForeignKey('administrador.idAdmin'))
    idProv = db.Column(db.Integer, db.ForeignKey('proveedor.idProv'))
    