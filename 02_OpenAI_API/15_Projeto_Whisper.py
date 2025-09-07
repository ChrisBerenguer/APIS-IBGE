import openai
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

from io import BytesIO
from playsound import playsound


import speech_recognition as sr

_ = load_dotenv(find_dotenv())

client = openai.Client()

ARQUIVO_AUDIO = 'falta_assistant.mp3'

recognizer = sr.Recognizer()

def grava_audio():
    with sr.Microphone() as source:
        print('Ouvindo...')
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        
    return audio


def trancricao_audio(audio):
    wav_data = BytesIO(audio.get_wav_data())
    wav_data.name = 'audio_teste.wav'
    transcricao = client.audio.transcriptions.create(
        model='whisper-1',
        file=wav_data
    )

    return transcricao.text


def completa_texto(mensagens):
    resposta = client.chat.completions.create(
        messages=mensagens,
        model='gpt-3.5-turbo-0125',
        max_tokens=1000,
        temperature=0
    )

    return resposta.choices[0].message.content


def cria_audio(texto):
    import time
    timestamp = int(time.time())
    arquivo = f'assistant_response_{timestamp}.mp3'
    
    # Remove arquivo anterior se existir
    if Path(arquivo).exists():
        Path(arquivo).unlink()
    
    resposta = client.audio.speech.create(
        model='tts-1',
        voice='onyx',
        input=texto
    )
    resposta.write_to_file(arquivo)
    return arquivo


def roda_audio_assistant(arquivo):
    playsound(arquivo)


if __name__ == '__main__':
    mensagens = []

    while True:
        audio = grava_audio()
        transcricao = trancricao_audio(audio)
        mensagens.append({'role': 'user', 'content': transcricao})
        print(f'User: {mensagens[-1]["content"]}')
        resposta = completa_texto(mensagens)
        mensagens.append({'role': 'assistant', 'content': resposta})
        print(f'Assistant: {resposta}')
        arquivo_audio = cria_audio(mensagens[-1]["content"])   
        roda_audio_assistant(arquivo_audio)     
    
    