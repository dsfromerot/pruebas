from flask import jsonify
from flask_oidc import OpenIDConnect
from .config import app, oidc

# Datos hardcodeados
pruebas = [
    {"fecha_radiografia": "2023-10-01", "informe": "Fractura de brazo", "nombre_doctor": "Dr. Smith"},
    {"fecha_radiografia": "2023-10-02", "informe": "Tumor benigno", "nombre_doctor": "Dr. Johnson"}
]

@app.route('/prueba', methods=['GET'])
@oidc.accept_token(True)
def get_prueba():
    return jsonify(pruebas)
