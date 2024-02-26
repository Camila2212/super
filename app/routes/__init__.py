from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import routesAdministrador, routesClientes, routesProductos, routesProveedores, routesDetallesCompra, routesFacturasCompra, routesFacturasVenta ,routesDetallesVenta, auth, routesCarrito