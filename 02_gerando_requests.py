import requests

url = "https://httpbin.org/get"

resposta = requests.get(url)

resposta.raise_for_status()

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f'Não é possível fazer request. Erro {e}')

else:
    print("Resultado:")
    print(resposta.json())

'''if resposta.status_code == 200:
    print("Requisição feita com sucesso")
else:
    print("Requisição falhou")'''

# print(resposta.status_code)




# print(resposta.json())







