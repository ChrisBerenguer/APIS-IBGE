from openai import OpenAI
from dotenv import load_dotenv  # Para carregar variáveis de ambiente de um arquivo .env
import os  # Para acessar variáveis de ambiente do sistema

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key is None:
    raise ValueError("A chave da API não foi encontrada no arquivo .env.")

client = OpenAI(api_key=openai_api_key)


def geracao_texto(mensagens):

    resposta = client.chat.completions.create(
        messages=mensagens,
        model='gpt-3.5-turbo-0125',
        max_tokens=1000,
        temperature=0,
        stream=True
    )


    print('Assistant ', end='' )
    texto_completo = ''

    for resposta_stream in resposta:
        texto = resposta_stream.choices[0].delta.content
        if texto:
            print(texto, end='')
            texto_completo += texto
    print()

    mensagens.append({'role': 'assistant', 'content': texto_completo})
    return mensagens



if __name__ == '__main__':

    print('Bem-vindo ao ChatGPT da Shopee: ')
    mensagens = []
    while True:
        input_usuario = input('User: ')
        mensagens.append({'role': 'user','content': input_usuario})

        mensagens = geracao_texto(mensagens)
