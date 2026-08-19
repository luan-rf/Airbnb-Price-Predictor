#  Airbnb Price Predictor

Aplicação interativa desenvolvida em **Streamlit** que utiliza um modelo de Machine Learning para prever a diária ideal de imóveis no Airbnb com base em suas características e localização.

---

## 🎯 Objetivo

Ajudar proprietários e anfitriões a definirem preços competitivos para suas acomodações, reduzindo a incerteza na precificação e otimizando a rentabilidade do imóvel através de Análise de Dados e Aprendizado de Máquina.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Interface Web:** [Streamlit](https://streamlit.io/)
* **Manipulação de Dados:** Pandas
* **Machine Learning:** Scikit-Learn
* **Persistência do Modelo:** Joblib

---

## 📋 Funcionalidades

* **Entrada de Atributos Numéricos:** Latitude, longitude, número de quartos, banheiros, camas, hóspedes, noites mínimas, etc.
* **Opções Binárias:** Status de Superhost e Reserva Instantânea (*Instant Bookable*).
* **Categorias Personalizadas:** Tipo de propriedade, tipo de acomodação e política de cancelamento.
* **Transformação Dinâmica:** Aplicação automática de *One-Hot Encoding* para adequar os dados ao formato esperado pelo modelo.
* **Previsão em Tempo Real:** Retorna o preço estimado em reais (R$) de forma instantânea.

---

## 📂 Estrutura do Repositório

```text
.
├── app.py              # Script principal da aplicação Streamlit
├── modelo.joblib       # Modelo de Machine Learning treinado
├── requirements.txt    # Lista de dependências do projeto
└── README.md           # Documentação do projeto
🚀 Como Executar o Projeto Localmente
Pré-requisitos
Certifique-se de ter o Python (versão 3.8 ou superior) instalado em sua máquina.

Clone o repositório:

Bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
Instale as dependências:

Bash
pip install -r requirements.txt
Execute a aplicação Streamlit:

Bash
streamlit run app.py
Abra o navegador no endereço indicado (geralmente http://localhost:8501).
