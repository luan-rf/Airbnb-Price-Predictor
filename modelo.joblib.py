import pandas as pd
import streamlit as st
import joblib


@st.cache_resource
def carregar_modelo():
    # O argumento mmap_mode='r' ajuda a ler modelos grandes consumindo menos RAM
    return joblib.load('modelo.joblib', mmap_mode='r')


        
x_numericos = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0,
               'minimum_nights': 0, 'ano': 0, 'mes': 0, 'n_amenities': 0, 'host_listings_count': 0}

x_tf = {'host_is_superhost': 0, 'instant_bookable': 0}

x_listas = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Outros', 'Serviced apartment'],
            'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
            'cancellation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']
            }


st.title("Previsão de Preço de Imóveis - Airbnb")

# 1. Criação dos campos numéricos salvando o valor direto no dicionário
for item in x_numericos: 
    # Usamos o valor padrão do dicionário como 'value'
    if item in ['latitude', 'longitude']:
        x_numericos[item] = st.number_input(f"{item}", value=0.0, step=0.00001, format="%.5f")
    else:
        x_numericos[item] = st.number_input(f"{item}", value=0)

# 2. Criação dos campos binários (Sim/Não) salvando no dicionário
for item in x_tf: 
    opcao = st.selectbox(f"{item}", ("Sim", "Não"))
    # Converte "Sim" para 1 e "Não" para 0 (comum em modelos de machine learning)
    x_tf[item] = 1 if opcao == "Sim" else 0

# 3. Criação dos campos de listas salvando no dicionário
# Para modelos com variáveis categóricas tratadas (Ex: OneHotEncoding), 
# precisamos mapear qual texto o usuário escolheu.
dicionario_selecionados = {}
for item in x_listas:
    dicionario_selecionados[item] = st.selectbox(f"{item}", x_listas[item])


# Botão para executar a previsão
# Botão para executar a previsão
if st.button("Prever preço do imóvel"):
    
    # 1. Unir os dicionários simples que já guardam números (numéricos e booleanos)
    dicionario_valores = {}
    dicionario_valores.update(x_numericos)
    dicionario_valores.update(x_tf)
    
    # 2. Fazer o tratamento das listas (One-Hot Encoding) mudando para 1 e 0
    for categoria, lista_opcoes in x_listas.items():
        opcao_escolhida = dicionario_selecionados[categoria]
        
        for opcao in lista_opcoes:
            nome_coluna = f"{categoria}_{opcao}"
            
            if opcao == opcao_escolhida:
                dicionario_valores[nome_coluna] = 1
            else:
                dicionario_valores[nome_coluna] = 0
                
    # 3. Transformar o dicionário final em um DataFrame
    dados_previsao = pd.DataFrame([dicionario_valores])
    
    # 🔥 LINHA DE SEGURANÇA: Garante que as colunas estejam na MESMA ordem do treino
    modelo = carregar_modelo()

    if hasattr(modelo, 'feature_names_in_'):
        dados_previsao = dados_previsao[modelo.feature_names_in_]
    
    # 4. Rodar o modelo
    resultado = modelo.predict(dados_previsao)
    st.success(f"O preço previsto para o imóvel é: R$ {resultado[0]:.2f}")
    
    st.write("Dados estruturados prontos para enviar ao modelo:")
    st.dataframe(dados_previsao)