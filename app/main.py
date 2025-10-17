import os
import sys
from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from config.database import db
from config.jwt import JWT_SECRET_KEY
from controllers.users_controller import user_bp
from controllers.movies_controller import movies_bp

# --- Asegurar que el path sea correcto ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# --- Crear la app ---
app = Flask(__name__)

# --- Configuración ---
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY

# --- Inicializar extensiones ---
db.init_app(app)
jwt = JWTManager(app)

# --- Registrar blueprints ---
app.register_blueprint(user_bp, url_prefix="/auth")
app.register_blueprint(movies_bp, url_prefix="/movies")

# --- Ruta para la interfaz ---
@app.route("/")
def home():
    return render_template("index.html")

# --- Crear tablas automáticamente ---
with app.app_context():
    db.create_all()

# --- Mostrar rutas registradas ---
print("🔍 Rutas registradas:")
for rule in app.url_map.iter_rules():
    print(rule)

# --- Ejecutar servidor ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
