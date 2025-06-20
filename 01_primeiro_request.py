import requests

url = "https://httpbin.org/post"


# Dados a serem enviados -- Request Body (dados que serão enviados para o banco de dados)
dados ={

    "meus_dados": [1,2,3],
    "pessoa": {
        "nome":"juca",
        "mestre": True
    
    
    }
    
}

# Parametros a serem enviados -- Request URL: Filtros, paramteros, etc 
parametro = {
    "dataInicio": "2025-01-01",
    "dataFim": "2025-04-02",
}


resposta = requests.post(url, json=dados, params=parametro)

print(resposta.request.url)
print(resposta.json())







