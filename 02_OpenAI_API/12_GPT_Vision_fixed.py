import openai
import base64
from dotenv import load_dotenv, find_dotenv

# Carregar variáveis de ambiente
_ = load_dotenv(find_dotenv())

# Criar cliente OpenAI
client = openai.Client()

# Função correta para codificar imagem em base64
def encode_image(caminho_imagem):
    with open(caminho_imagem, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Caminho da imagem (ajuste para o caminho correto no Windows)
caminho_imagem = r'C:\Users\chris\OneDrive\Documentos\Asimov_Academy\AI_Agents\02_OpenAI_API\Explorando a API da OpenAI\arquivos\vision\celulas.jpg'

# Codificar a imagem
base_64_image = encode_image(caminho_imagem)

# Fazer requisição para análise de imagem
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text': 'quantas celulas aparecem na imagem?'},
                {'type': 'image_url', 'image_url': {'url': f'data:image/jpg;base64,{base_64_image}'}}
            ]
        }
    ],
    max_tokens=1000
)

# Exibir a resposta
print(response.choices[0].message.content) 