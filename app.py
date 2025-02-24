from flask import Flask, jsonify
from flask_oidc import OpenIDConnect

app = Flask(__name__)

# Configuración de Keycloak
app.config.update({
    'SECRET_KEY': 'secret',
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
})
oidc = OpenIDConnect(app)

# Datos hardcodeados
pruebas = [
    {"fecha_radiografia": "2023-10-01", "informe": "Fractura de brazo", "nombre_doctor": "Dr. Smith"},
    {"fecha_radiografia": "2023-10-02", "informe": "Tumor benigno", "nombre_doctor": "Dr. Johnson"}
]

@app.route('/prueba', methods=['GET'])
@oidc.accept_token(True)  # Protege la ruta con Keycloak
def get_prueba():
    return jsonify(pruebas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
