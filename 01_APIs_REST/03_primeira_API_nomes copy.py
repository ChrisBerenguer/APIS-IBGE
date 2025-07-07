import requests
from pprint import pprint # Biblioteca que printa de forma mais estruturada do que o print convencional
nome = 'Ariel'


url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

parametros = {
    'sexo':'M',
    'localidade': 33,

}



resposta = requests.get(url, params=parametros)

print(f'Extraído de: {resposta.request.url}')

try:
    resposta.raise_for_status()
    
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    resultado = None

else: 
    resultado = resposta.json()

    pprint(resultado[0]['res'])