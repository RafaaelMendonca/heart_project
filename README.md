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
│   └── EDA.ipynb
├── pickle/
│   └── svm_model.pkl
├── utils/
│   ├── __init__.py
│   └── preprocessing.py
```

### Descrição dos Diretórios

- **`dataBase/`**: Contém o arquivo de dados `heart.csv` utilizado para análise e treinamento do modelo.
- **`notebooks/`**: Contém o notebook `EDA.ipynb` com a análise exploratória dos dados (EDA) e visualizações.
- **`pickle/`**: Armazena o modelo treinado em formato `.pkl`.
- **`utils/`**: Contém scripts auxiliares, como funções de pré-processamento.

## Etapas do Projeto

O projeto segue a metodologia CRISP-DM, com as seguintes etapas:

1. **Entendimento do Negócio**
2. **Entendimento dos Dados**
3. **Preparação dos Dados**
4. **Desenvolvimento do Estudo**
5. **Validação**
6. **Implementação e Acompanhamento**

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
  - `pandas`, `numpy`: Manipulação e análise de dados.
  - `matplotlib`, `seaborn`: Visualização de dados.
  - `scikit-learn`: Modelagem e avaliação de aprendizado de máquina.
  - `fontTools`: Utilizada em scripts auxiliares.

## ✅ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/RafaaelMendonca/heart_project.git
   cd heart-project
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate    # No Linux/macOS
   venv\Scripts\activate.bat   # No Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o notebook de análise exploratória:  
   Abra o arquivo `notebooks/EDA.ipynb` em um ambiente como Jupyter Notebook ou VS Code.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.