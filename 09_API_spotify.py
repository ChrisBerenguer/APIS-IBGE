
import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint  # Para imprimir o resultado de forma mais "bonita" e legível
import dotenv
import os

dotenv.load_dotenv()

id_cliente = os.environ['SPOTIFY_CLIENT_ID']
cliente_secret = os.environ['SPOTIFY_CLIENT_SECRET']

# Definindo a URL da API que vamos acessar
url = "https://accounts.spotify.com/api/token"

# Criando a string de autenticação em Base64
autenticacao = HTTPBasicAuth(username=id_cliente, password=cliente_secret)


# Configurando os headers da requisição
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
    resultado = None

else: 
        # Se não houve erro, converte a resposta para JSON
    resultado = resposta.json()



token = resultado['access_token']

id_artista = "2wOqMjp9TyABvtHdOSOTUS"
url=f"https://api.spotify.com/v1/artists/{id_artista}"

headers = {
    'Authorization': f'Bearer {token}'
}

resposta = requests.get(url=url, headers=headers)
pprint(resposta.json())