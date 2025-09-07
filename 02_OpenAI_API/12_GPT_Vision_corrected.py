import openai
from dotenv import load_dotenv, find_dotenv

# Carregar variáveis de ambiente
_ = load_dotenv(find_dotenv())

# Criar cliente OpenAI
client = openai.Client()

# Fazer requisição para análise de imagem
response = client.chat.completions.create(
    model="gpt-4o",  # Modelo atualizado (gpt-4-vision-preview foi descontinuado)
    messages=[
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text': 'descreva a imagem fornecida'},
                {'type': 'image_url', 'image_url': {'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg'}}
            ]
        }
    ]
)

# Exibir a resposta
print(response.choices[0].message.content) 