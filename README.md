# Heart Disease Prediction Project

Este projeto tem como objetivo criar um modelo de aprendizado de máquina para prever o risco de doenças cardíacas com base em dados clínicos. A ideia é auxiliar médicos e profissionais da saúde a realizar diagnósticos mais rápidos e precisos, além de identificar padrões nos dados que possam melhorar a compreensão dos fatores de risco.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

heart-project/
├── README.md
├── requirements.txt
├── dataBase/
│ └── heart.csv
├── new_venv/
│ └── (ambiente virtual Python)
├── notebooks/
│ └── EDA.ipynb
├── pickle/
│ └── svm_model.pkl
├── utils/
│ ├── init.py
│ └── preprocessing.py


### Descrição dos Diretórios

- **`dataBase/`**: Contém o arquivo de dados `heart.csv` utilizado para análise e treinamento do modelo.
- **`new_venv/`**: Ambiente virtual Python com as dependências do projeto.
- **`notebooks/`**: Contém o notebook `EDA.ipynb` com a análise exploratória dos dados (EDA) e visualizações.
- **`pickle/`**: Armazena o modelo treinado em formato `.pkl`.
- **`utils/`**: Contém scripts auxiliares, como funções de pré-processamento.

## Etapas do Projeto

O projeto segue a metodologia CRISP-DM, com as seguintes etapas:

1. **Entendimento do Negócio**: Identificar o problema e os objetivos do projeto.
2. **Entendimento dos Dados**: Analisar a estrutura dos dados, verificar valores nulos, duplicados e outliers.
3. **Preparação dos Dados**: Realizar o pré-processamento, incluindo normalização e divisão em conjuntos de treino e teste.
4. **Desenvolvimento do Estudo**: Treinar modelos de aprendizado de máquina, como SVM e Random Forest.
5. **Validação**: Avaliar o desempenho dos modelos utilizando métricas como acurácia e matriz de confusão.
6. **Implementação e Acompanhamento**: Implementar o modelo final e monitorar seu desempenho.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
  - `pandas`, `numpy`: Manipulação e análise de dados.
  - `matplotlib`, `seaborn`: Visualização de dados.
  - `scikit-learn`: Modelagem e avaliação de aprendizado de máquina.
  - `fontTools`: Utilizada em scripts auxiliares.

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/RafaaelMendonca/heart_project.git
   cd heart-project

2. Ative o ambiente virtual:
    source new_venv/bin/activate

3. Instale as dependências:
    pip install -r requirements.txt

4. Execute o notebook de análise exploratória: 
    Abra o arquivo notebooks/EDA.ipynb em um ambiente como Jupyter Notebook ou VS Code.

**Contribuição**
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

