from flask import Flask, jsonify
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
oauth = OAuth(app)

# Configura Keycloak
oauth.register(
    name='keycloak',
    client_id='pruebas',  # Cambia el client_id para este microservicio
    client_secret='z6HWn75LP7qSq5JTdmrEbDOzrRjq1k8O',  # Cambia el client_secret
    authorize_url='http://100.124.235.117:8080/auth/realms/hospital-realm/protocol/openid-connect/auth',
    authorize_params=None,
    access_token_url='http://100.124.235.117:8080/auth/realms/hospital-realm/protocol/openid-connect/token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri='http://100.93.128.110:5002/callback',  # Cambia el puerto
    client_kwargs={'scope': 'openid profile email'},
)

@app.route('/pruebas', methods=['GET'])
def get_pruebas():
    token = oauth.keycloak.authorize_access_token()
    if not token:
        return jsonify({"error": "Acceso no autorizado"}), 401
    pruebas = [
        {"fecha_radiografia": "2023-10-01", "informe": "Fractura de brazo", "nombre_doctor": "Dr. Smith"},
        {"fecha_radiografia": "2023-10-02", "informe": "Tumor benigno", "nombre_doctor": "Dr. Johnson"}
    ]
    return jsonify(pruebas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)  # Cambia el puerto
