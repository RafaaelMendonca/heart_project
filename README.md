# Heart Disease Prediction Project

Este projeto tem como objetivo criar um modelo de aprendizado de máquina para prever o risco de doenças cardíacas com base em dados clínicos. A ideia é auxiliar médicos e profissionais da saúde a realizar diagnósticos mais rápidos e precisos, além de identificar padrões nos dados que possam melhorar a compreensão dos fatores de risco.

## 📁 Estrutura do Projeto

```
heart-project/
├── README.md
├── requirements.txt
├── dataBase/
│   └── heart.csv
├── notebooks/
│   └── heart_project.ipynb
├── pickle/
│   └── svm_model.pkl
│   └── scaler.pkl
├── utils/
│   ├── __init__.py
│   └── preprocessing.py
├── flask_api/
│   ├── app.py
│   └── model_utils.py
```

### Descrição dos Diretórios

- **`dataBase/`**: Contém o arquivo de dados `heart.csv` utilizado para análise e treinamento do modelo.
- **`notebooks/`**: Contém o notebook `heart_project.ipynb` com a análise exploratória dos dados e implementação do modelo.
- **`pickle/`**: Armazena o modelo e o MinMaxScaler treinado em formato `.pkl`.
- **`utils/`**: Contém scripts auxiliares, como funções de pré-processamento.
- **`flask_api/`**: Contém os arquivos da API desenvolvida com Flask para servir o modelo de machine learning via HTTP.

## Etapas do Projeto

O projeto segue a metodologia CRISP-DM, com as seguintes etapas:

1. **Entendimento do Negócio**
2. **Entendimento dos Dados**
3. **Preparação dos Dados**
4. **Desenvolvimento do Estudo**
5. **Validação**
6. **Implementação e Acompanhamento**

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
  - `pandas`: Manipulação e análise de dados.
  - `matplotlib`, `seaborn`: Visualização de dados.
  - `scikit-learn`, `scipy`, `joblib`: Modelagem e serialização.
  - `Flask`: Desenvolvimento da API.

## ✅ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/RafaaelMendonca/heart_project.git
cd heart-project
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate    # No Linux/macOS
venv\Scripts\activate.bat   # No Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o notebook de análise exploratória (opcional)

Abra o arquivo `notebooks/heart_project.ipynb` em um ambiente como Jupyter Notebook ou VS Code para visualizar a análise e treinamento do modelo.

### 5. Execute a API Flask

```bash
cd flask_api
python app.py
```

A API estará disponível em: `http://127.0.0.1:5000/`

Você pode fazer requisições POST para o endpoint `/predicao` com um JSON como:

```json
{
    "age": 63,
    "sex": 1,
    "cp": 3,
    "trtbps": 145,
    "chol": 233,
    "fbs": 1,
    "restecg": 0,
    "thalachh": 150,
    "exng": 0,
    "oldpeak": 2.3,
    "slp": 0,
    "caa": 0,
    "thall": 1
}
```

Resposta esperada:

```json
{
    "confianca": 82.12,
    "predicao": "Doença cardíaca"
}
```

```json
{
    "age": 57,
    "sex": 0,
    "cp": 0,
    "trtbps": 140,
    "chol": 241,
    "fbs": 0,
    "restecg": 1,
    "thalachh": 123,
    "exng": 1,
    "oldpeak": 0.2,
    "slp": 1,
    "caa": 0,
    "thall": 3
}
```

```
{
  "confianca": 67.0,
  "predicao": "Healthy"
}
```


## 🤝 Contribuição

Contribuições são bem-vindas!
