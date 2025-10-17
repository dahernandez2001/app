import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from flask import Flask
from flask_jwt_extended import JWTManager
from config.database import db
from config.jwt import JWT_SECRET_KEY, JWT_ACCESS_TOKEN_EXPIRES
from controllers.users_controller import user_bp
from controllers.movies_controller import movies_bp

app = Flask(__name__)

# Configuración
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
# opcional: expiración
# from datetime import timedelta
# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=JWT_ACCESS_TOKEN_EXPIRES)

# Inicializar extensiones
db.init_app(app)
jwt = JWTManager(app)

# Registrar blueprints
app.register_blueprint(user_bp, url_prefix="/auth")
app.register_blueprint(movies_bp, url_prefix="/movies")

# Crear tablas
with app.app_context():
    db.create_all()

print("🔍 Rutas registradas:")
for rule in app.url_map.iter_rules():
    print(rule)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
