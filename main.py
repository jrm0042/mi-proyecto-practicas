from flask import Flask, jsonify
import mi_script  # tu código adaptado
import logging  # <-- Importamos logging

# Configuración básica de logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def home():
    logging.info("Ruta '/' accedida")  # <-- Añadimos log
    return "<h1>¡Bienvenido a mi aplicación Flask con Docker!</h1>"

@app.route('/procesar')
def procesar():
    resultado = mi_script.procesar()
    logging.info(f"Resultado del procesamiento: {resultado}")  # <-- Añadimos log
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

