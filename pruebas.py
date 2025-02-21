from flask import Flask, jsonify

app = Flask(__name__)

pruebas = [
    {"fecha_radiografia": "2023-10-01", "informe": "Fractura", "nombre_doctor": "Dr. Smith"},
    {"fecha_radiografia": "2023-10-02", "informe": "Tumor", "nombre_doctor": "Dr. Johnson"}
]

@app.route('/pruebas', methods=['GET'])
def get_pruebas():
    return jsonify(pruebas)

if __name__ == '__main__':
    app.run(port=5002)