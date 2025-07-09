# Importando as bibliotecas necessárias
import requests  # Para fazer requisições HTTP
from requests.auth import HTTPBasicAuth  # Para autenticação básica HTTP
from pprint import pprint  # Para imprimir dados de forma mais organizada
import dotenv  # Para carregar variáveis de ambiente de um arquivo .env
import os  # Para acessar variáveis de ambiente do sistema
import streamlit as st  # Framework para criar aplicações web

# Carrega as variáveis de ambiente do arquivo .env
dotenv.load_dotenv()

# Função para autenticar na API do Spotify e obter um token de acesso
def autenticar():
    # Obtém o ID do cliente e o segredo do cliente do arquivo .env
    id_cliente = os.environ['SPOTIFY_CLIENT_ID']
    cliente_secret = os.environ['SPOTIFY_CLIENT_SECRET']

    # Cria um objeto de autenticação básica HTTP com as credenciais
    autenticacao = HTTPBasicAuth(username=id_cliente, password=cliente_secret)
    
    # URL da API do Spotify para obter o token
    url = "https://accounts.spotify.com/api/token"

    # Corpo da requisição POST - indica que estamos usando credenciais do cliente
    body = {
        'grant_type': 'client_credentials'
    }

    # Faz uma requisição POST para obter o token de acesso
    resposta = requests.post(url=url, data=body, auth=autenticacao)

    # Tratamento de erros na requisição
    try:
        # Verifica se houve erro na requisição (como 404, 500, etc)
        resposta.raise_for_status()
            
    except requests.HTTPError as e:
        # Se houve erro, imprime a mensagem e retorna None como token
        print(f"Erro no request: {e}")
        token = None

    else: 
        # Se não houve erro, extrai o token da resposta JSON
        token = resposta.json()['access_token']
        print('Token obtido com sucesso')
    return token

# Função para buscar um artista na API do Spotify
def buscar_artista(nome_artista, headers):
    # URL da API para busca
    url = "https://api.spotify.com/v1/search"
    
    # Parâmetros da busca: nome do artista e tipo (artista)
    parametros = {
        'q': nome_artista,
        'type': 'artist',
    }

    # Faz a requisição GET com os parâmetros e headers (que contém o token)
    resposta = requests.get(url, params=parametros, headers=headers)
    
    try:
        # Tenta pegar o primeiro resultado da lista de artistas
        primeiro_resultado = resposta.json()['artists']['items'][0]
    except IndexError:
        # Se não encontrar nenhum artista, retorna None
        primeiro_resultado = None
        
    return primeiro_resultado

# Função para buscar as músicas mais populares de um artista
def busca_top_musicas(id_artista, headers):
    # Monta a URL com o ID do artista para buscar as top músicas
    url = f"https://api.spotify.com/v1/artists/{id_artista}/top-tracks"
    
    # Faz a requisição GET
    resposta = requests.get(url, headers=headers)
    
    # Retorna apenas a lista de músicas da resposta JSON
    return resposta.json()['tracks']

# Função principal que será executada quando o script rodar
def main():
    # Configura o título da página web
    st.title('Projeto Spotify Web')
    
    # Adiciona uma descrição com link para a documentação da API
    st.write('Dados da API do Spotify: https://developer.spotify.com/documentation/web-api')
    
    # Cria um campo de texto para o usuário digitar o nome do artista
    nome_artista = st.text_input('Procure um artista: ')
    
    # Se o usuário não digitou nada, para a execução
    if not nome_artista:
        st.stop()

    # Obtém o token de acesso
    token = autenticar()
    
    # Cria os headers para as requisições, incluindo o token
    headers = {
        'Authorization': f'Bearer {token}'
    }

    # Busca o artista na API
    artista = buscar_artista(nome_artista=nome_artista, headers=headers)
    
    # Se não encontrou o artista, mostra mensagem de aviso e para
    if not artista:
        st.warning(f'Artista {nome_artista} não encontrado')
        st.stop()

    # Extrai informações do artista: ID, nome e popularidade
    id_artista = artista['id']
    nome_artista = artista['name']
    popularidade_artista = artista['popularity']

    # Busca as músicas mais populares do artista
    melhores_musicas = busca_top_musicas(id_artista=id_artista, headers=headers)

    # Mostra o nome do artista e sua popularidade
    st.subheader(f'Artista: {nome_artista} | Popularidade {popularidade_artista}')

    # Para cada música, mostra seu nome (como link), e popularidade
    for musica in melhores_musicas:
        nome_musica = musica['name']
        poularidade_musica = musica['popularity']
        link_musica = musica['external_urls']['spotify']
        
        # Cria um link clicável usando markdown
        link_em_markdown = f'[{nome_musica}]({link_musica})'
        
        # Mostra o link e a popularidade
        st.write(f'{link_em_markdown} | Popularidade: {poularidade_musica}')

# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == '__main__':
    # Chama a função principal
    main()

# Para executar a aplicação, use no terminal:
# streamlit run 10_projeto_app_spotify_final.py