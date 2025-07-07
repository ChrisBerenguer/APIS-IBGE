import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint  # Para imprimir o resultado de forma mais "bonita" e legível
import dotenv
import os
import streamlit as st

dotenv.load_dotenv()


def autenticar():

    id_cliente = os.environ['SPOTIFY_CLIENT_ID']
    cliente_secret = os.environ['SPOTIFY_CLIENT_SECRET']

    # Criando a string de autenticação em Base64
    autenticacao = HTTPBasicAuth(username=id_cliente, password=cliente_secret)
    # Definindo a URL da API que vamos acessar
    url = "https://accounts.spotify.com/api/token"

    # Configurando os headers da requisição -- Vem na documentação da API
    body = {
        'grant_type': 'client_credentials'
    }

    # Fazendo uma requisição GET para a API, passando a URL e os headers
    resposta = requests.post(url=url, data=body, auth=autenticacao)

    # Bloco try-except para tratar erros de requisição (ex: site fora do ar, URL errada, etc)
    try:
            # Verifica se houve algum erro na requisição (ex: 404, 500, etc)
        resposta.raise_for_status()
            
    except requests.HTTPError as e:
            # Caso ocorra um erro HTTP, imprime a mensagem de erro e define resultado como None
        print(f"Erro no request: {e}")
        token = None

    else: 
            # Se não houve erro, converte a resposta para JSON
        token = resposta.json()['access_token']
        print('Token obtido com sucesso')
    return token


def buscar_artista(nome_artista, headers):
    url="https://api.spotify.com/v1/search"
    parametros = {
        'q': nome_artista,
        'type': 'artist',

    }

    resposta = requests.get(url, params=parametros, headers=headers)
    
    try:
        primeiro_resultado = resposta.json()['artists']['items'][0]
    except IndexError:
        primeiro_resultado = None
        
    return primeiro_resultado


def busca_top_musicas(id_artista, headers):
    url = f"https://api.spotify.com/v1/artists/{id_artista}/top-tracks"
    resposta = requests.get(url, headers=headers)
    return resposta.json()['tracks']


def main():
    st.title('Projeto Spotify Web')
    st.write('Dados da API do Spotify: https://developer.spotify.com/documentation/web-api')
    nome_artista = st.text_input('Procure um artista: ')
    if not nome_artista:
        st.stop()



    token = autenticar()
    headers = {
        'Authorization': f'Bearer {token}'
    }

    artista = buscar_artista(nome_artista=nome_artista, headers=headers)
    if not artista:
        st.warning(f'Artista {nome_artista} não encontrado')
        st.stop()

    id_artista = artista['id']
    nome_artista = artista['name']
    popularidade_artista = artista['popularity']


    melhores_musicas = busca_top_musicas(id_artista=id_artista, headers=headers)

    st.subheader(f'Artista: {nome_artista} | Popularidade {popularidade_artista}')




    for musica in melhores_musicas:
        nome_musica = musica['name']
        poularidade_musica = musica['popularity']
        link_musica = musica['external_urls']['spotify']
        link_em_markdown = f'[{nome_musica}]({link_musica})'
        st.write(f'{link_em_markdown} | Popularidade: {poularidade_musica}')



if __name__ == '__main__':
    main()


# streamlit run 10_projeto_app_spotify_final.py