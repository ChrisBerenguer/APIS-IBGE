import requests   
from pprint import pprint 
import pandas as pd


import streamlit as st




# Função para obter a frequência de um nome por estado
def pegar_nome_por_decada(nome):
    # Define a URL da API do IBGE para obter informações nomes brasileiros
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

 

    # Faz a requisição e obtém os dados de frequência
    dados_decadas = fazer_request(url=url)
    if not dados_decadas:
        return{}

    
    dict_decadas = {}
    # Para cada estado, extrai o ID e a frequência do nome e adiciona ao dicionário
    for dados in dados_decadas[0]['res']:
       decada = dados['periodo']
       quantidade = dados['frequencia']
       dict_decadas[decada] = quantidade
    return dict_decadas
        

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
def main():
    st.title('web app nomes')
    st.write('Dados do IBGE - Fonte: https://servicodados.ibge.gov.br/api/docs/nomes?versao=2')
    
    nome = st.text_input('Consulte um nome:')

    if not nome:
        st.stop()

    dict_decadas = pegar_nome_por_decada(nome)
    if not dict_decadas:
        st.warning(f'Nenhum dado encontrado para o nome {nome}')
        st.stop()

    if not dict_decadas:
        st.warning('Nenhum dado encontrado')
        st.stop()

    df = pd.DataFrame.from_dict(dict_decadas, orient="index", columns=["Frequência"])
    df.index.name = "Década"
    # Extrai o ano inicial da década para usar no eixo x como número
    df = df.reset_index()
    df['Ano'] = df['Década'].str.extract(r'(\d{4})').astype(int)
    df = df.sort_values('Ano')
    df = df.set_index('Ano')  # Agora o índice é o ano

    col1, col2 = st.columns([0.3, 0.7])
    with col1:
        st.write('Frequência por década')
        st.dataframe(df)

    with col2:
        st.write('Evolução no tempo')
        st.line_chart(df["Frequência"])




   

    

# Executa a função principal se o script for executado diretamente
if __name__ == '__main__':
    main()


# Rodar Streamlit: No Terminal, escrever 'streamlit run .\05_projeto.py'