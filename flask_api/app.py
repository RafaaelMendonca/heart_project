import sys
import os
from flask_cors import CORS

# Adiciona o caminho da raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pickle
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app)

with open('../pickle/svm_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('../pickle/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/predicao', methods=['POST'])
def predicao():
    dados = request.json
    campos_necessarios = ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall'] 

    if not all (k in dados for k in campos_necessarios):
        return jsonify({"error": "Dados incompletos"}), 400
    
    for campo in campos_necessarios:
        valor = dados[campo]

        try:
            valor_nun = float(valor)
        except ValueError:
            return jsonify({"error": f"Campo {campo} deve ser um número"}), 400
    
    df = pd.DataFrame([dados])
    df = scaler.transform(df)
    predicao = model.predict(df)
    probabilidade = model.predict_proba(df)[0]

    mapa_predicao = {
        0: "Healthy",
        1: "Heart Disease"
    }

    predicao_nome = mapa_predicao[predicao[0]]
    confianca = round(100 * float(probabilidade[predicao]), 2)
    return jsonify({
        "predicao": predicao_nome,
        "confianca": confianca
    })

if __name__ == '__main__':
    app.run(debug=True)
