import requests   


# Função para obter o dicionário de IDs e nomes dos estados brasileiros
def pegar_id_estados():
    # Define a URL da API do IBGE para obter informações dos estados brasileiros
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

    # Define os parâmetros da requisição (nesse caso, apenas 'view' como 'nivelado')
    parametros = {
        'view': 'nivelado',
    }
    # Faz a requisição e obtém os dados dos estados
    dados_dos_estados = fazer_request(url=url, params=parametros)
    dict_estado = {}
    # Para cada estado, extrai o ID e o nome e adiciona ao dicionário
    for dados in dados_dos_estados:
        id_estado = dados['UF-id']
        nome_estado = dados['UF-nome']
        dict_estado[id_estado] = nome_estado

    return dict_estado


# Função para obter a frequência de um nome por estado
def pegar_frequencia_nome_por_estado(nome):
    # Define a URL da API do IBGE para obter informações nomes brasileiros
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

    # Define os parâmetros da requisição (nesse caso, apenas 'groupBy' como 'UF')
    parametros = {
        'groupBy': 'UF',
    }

    # Faz a requisição e obtém os dados de frequência
    dados_frequencias = fazer_request(url=url, params=parametros)
    dict_frequencias = {}
    # Para cada estado, extrai o ID e a frequência do nome e adiciona ao dicionário
    for dados in dados_frequencias:
        id_estado = int(dados['localidade'])
        frequencia = dados['res'][0]['proporcao']
        dict_frequencias[id_estado] = frequencia

    return dict_frequencias
        

# Função genérica para fazer requisições GET e tratar erros
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


# Função principal que orquestra a busca e exibição dos dados
def main(nome):
    dict_estados = pegar_id_estados()  # Obtém o dicionário de estados
    dict_frequencia = pegar_frequencia_nome_por_estado(nome)  # Obtém a frequência do nome por estado
    print(f'Frequencia do nome {nome} nos estados (por 100.000 habitantes)')
   
    # Para cada estado, imprime o nome do estado e a frequência do nome
    for id_estado, nome_estado in dict_estados.items():
        frequencia_estado = dict_frequencia[id_estado]
        print(f'--> {nome_estado}: {frequencia_estado}')
    

# Executa a função principal se o script for executado diretamente
if __name__ == '__main__':
    main('Enzo')