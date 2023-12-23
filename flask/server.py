#from flask import Flask, request, jsonify

#app = Flask(__name__)

#@app.route('/submit_feedback', methods=['POST'])
#def submit_feedback():
    # Aquí procesas los datos de feedback
    #data = request.json
    #print(data)  # Solo para demostración
    # Aquí podrías agregar lógica para almacenar los datos en una base de datos, por ejemplo
    #return jsonify({"message": "Feedback recibido"}), 200

#if __name__ == '__main__':
    #app.run(debug=True, port=5000)


from flask import Flask, request, jsonify
from models.feedback_model import Feedback  # Importa el modelo Pydantic
from pydantic import ValidationError


app = Flask(__name__)

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    try:
        # Validación de datos con el modelo Pydantic
        feedback_data = Feedback(**request.json)
        # Aquí puedes procesar los datos validados, como almacenarlos en una base de datos
        print(feedback_data)  # Imprimir los datos validados
        return jsonify({"message": "Feedback recibido"}), 200
    except ValidationError as e:
        # Manejar errores de validación
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
