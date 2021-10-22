from flask import Flask, app, request
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return'El despliegue Funcionó!!!'


@app.route('/modelopredictivo', methods=['POST'])
def prediccion():
    json = request.get_json(force=True)
    xin = json['Cadena']
    xin = np.asarray(xin)
    xin = xin.reshape(1,13)
    # print("Servicio post")
    yout = model.predict(xin)
    print(yout)
    mensaje = ''
    for y_out in yout:
        mensaje = mensaje + 'El usuario@ es' + labels[y_out] + ' para una enfermedad cardiaca\n'
    
    return mensaje


    # Cargar modelo
pkl_filename = 'RandomForest.pkl'
with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)
    
labels = ['Negativo', 'Positivo'] # Etiquetas de datos


if __name__=='__name__':
    app.run()

