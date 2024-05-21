from flask import Flask
from src.routes.routes import init_routes

app = Flask(__name__)

# Inicializar las rutas
init_routes(app)

if __name__ == '__main__':
    app.run(debug=False, port=5000)