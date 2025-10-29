from flask import Flask, jsonify
import mi_script  # tu código adaptado

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hola mundo</h1>"

@app.route('/procesar')
def procesar():
    resultado = mi_script.procesar()
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
