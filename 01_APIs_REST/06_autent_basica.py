import base64  # Para codificar a string de autenticação em Base64 (requisito de algumas APIs)
import requests
from pprint import pprint  # Para imprimir o resultado de forma mais "bonita" e legível

usuario = "meu-usuario"
senha = "senha-secreta" 

# Montando a string de autenticação no formato "usuario:senha"
autent_string = f'{usuario}:{senha}'.encode() # Primeiro transformamos em bytes
autent_string = base64.b64encode(autent_string) # Depois codificamos em Base16 (errado para o caso de autenticação básica, mas vamos explicar depois)
autent_string = autent_string.decode() # Por fim, transformamos de volta para string (texto normal)

# Definindo a URL da API que vamos acessar
url = "https://httpbin.org/basic-auth/meu-usuario/senha-secreta"


# Criando o cabeçalho HTTP com a autenticação
headers = {
    'Authorization': f'Basic {autent_string}'
}

# Fazendo uma requisição GET para a API, passando a URL e os headers
resposta = requests.get(url=url, headers=headers)



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