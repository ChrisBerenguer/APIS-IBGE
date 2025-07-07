
import requests
from pprint import pprint  # Para imprimir o resultado de forma mais "bonita" e legível
import dotenv
import os
import streamlit as st


def fazer_request(url, params=None):
    resposta = requests.get(url, params=params)

    try:
        # Verifica se houve algum erro na requisição (ex: 404, 500, etc)
        resposta.raise_for_status()
        
    except requests.HTTPError as e:
        # Caso ocorra um erro HTTP, imprime a mensagem de erro e define resultado como None
        print(f"Erro no request: {e}")
        resultado = None

    else: 
        # Se não houve erro, converte a resposta para JSON
        resultado = resposta.json()

    return resultado

def pegar_tempo_para_local(local):
    dotenv.load_dotenv()
    token = os.environ['CHAVE_API_OPENWEATHER']
    # Definindo a URL da API que vamos acessar
    url = "https://api.openweathermap.org/data/2.5/weather"
    parametros = {
        'appid': token,
        'q': local,
        'units': 'metric',
        'lang': 'pt_br',
    }
    dados_tempo = fazer_request(url=url, params=parametros)
    return dados_tempo

def main():
    st.title('Web App Tempo')
    st.write('Dados da OpenWheather: https://openweathermap.org/current')

    local = st.text_input('Digite o nome da Cidade ')
    if not local:
        st.stop()


    dados_tempo = pegar_tempo_para_local(local=local)
    if not dados_tempo:
        st.warning(f"Dados não encontrados para a cidade: {local}")
        st.stop()


    clima_atual = dados_tempo['weather'][0]['description']
    temperatura = dados_tempo['main']['temp']
    sensacao_termica = dados_tempo['main']['feels_like']
    umidade = dados_tempo['main']['humidity']
    cobertura_nuvens = dados_tempo['clouds']['all']


    st.metric(label='Tempo atual', value=clima_atual)
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label='Temperatura', value=f'{temperatura} °C')
        st.metric(label='Sensação térmica', value=f'{sensacao_termica} °C')

    with col2:
        st.metric(label='Umidade', value=f'{umidade} %')
        st.metric(label='Cobertura de nuvens', value=f'{cobertura_nuvens} %')



    

if __name__ == '__main__':
    main()

# streamlit run 01_APIs_REST/08_projeto_app_clima.py