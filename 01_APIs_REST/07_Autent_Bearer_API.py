
import requests
from pprint import pprint  # Para imprimir o resultado de forma mais "bonita" e legível
import dotenv
import os

dotenv.load_dotenv()

token = os.environ['CHAVE_API_OPENWEATHER']

# Definindo a URL da API que vamos acessar
url = "https://api.openweathermap.org/data/2.5/weather"

parametros = {
    'appid': token,
    'q': 'Igarassu',
    'units': 'metric',

}

# Fazendo uma requisição GET para a API, passando a URL e os headers
resposta = requests.get(url=url, params=parametros)



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

# Exibe o resultado final de forma organizada
pprint(resultado)