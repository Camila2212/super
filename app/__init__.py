from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
db = SQLAlchemy()
login_manager = LoginManager()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(cliente_idCliente):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        from .models.Cliente import Cliente
        return Cliente.query.get(int(cliente_idCliente))

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    

    from app.routes import routesAdministrador, routesClientes, routesFacturasCompra, routesFacturasVenta, routesProductos, routesProveedores, routesDetallesCompra,routesDetallesVenta, routesCarrito
    app.register_blueprint(routesAdministrador.bp)
    app.register_blueprint(routesClientes.bp)
    app.register_blueprint(routesProductos.bp)
    app.register_blueprint(routesProveedores.bp)
    app.register_blueprint(routesFacturasVenta.bp)
    app.register_blueprint(routesFacturasCompra.bp)
    app.register_blueprint(routesDetallesCompra.bp)
    app.register_blueprint(routesDetallesVenta.bp)
    app.register_blueprint(routesCarrito.bp)

    


    return app