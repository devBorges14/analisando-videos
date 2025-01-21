"""
Este programa recolhe uma URL do youtube, transcreve o audio, e assim resumindo o vídeo 
usando a IA da OpenIA. Tendo um auto desempenho e agilidade.
"""
import openai
import whisper
import os
import re
from yt_dlp import YoutubeDL
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurar chave da OpenAI
API_KEY = os.getenv("API_KEY") # Pegando a API_KEY do arquivo .env
openai.api_key = API_KEY

# Recolher a URL do usuário
url_do_video = input("Digite sua URL: ")

# Extrair informações do vídeo
try:
    with YoutubeDL() as ydl:
        info = ydl.extract_info(url_do_video, download=False) # Extraindo os dados do youtube
        titulo_limpo = re.sub(r'[\\/*?:"<>|]', "", info['title']) # Retirando o titulo do vídeo e salvando-o em uma variavel para que seja salvo o arquivo com o titulo do youtube
        print(f"Título do vídeo: {info['title']}") # Printando o tiutulo do vídeo
except Exception as e:
    print(f"Ocorreu um erro ao extrair informações: {e}") # Tratamento simples
    exit()

# Configuração para baixar áudio
opcoes = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a', # Caso deseje mudar o formato do aúdio altere aqui (Arumme o código para suportar esse formato)
        'preferredquality': '192',
    }],
    'outtmpl': f'{titulo_limpo}.%(ext)s', # Arquvio será salvo com o titulo do youtube
}

# Baixar o áudio
try:
    with YoutubeDL(opcoes) as ydl:
        ydl.download([url_do_video]) # Baixando o audio do vídeio
    print("Áudio baixado com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro ao baixar o áudio: {e}")
    exit()

# Caminho do áudio
audio_do_video = f"{titulo_limpo}.m4a" 

# Verificar se o arquivo existe
if not os.path.exists(audio_do_video):
    print(f"Arquivo de áudio {audio_do_video} não encontrado.")
    exit()

# Transcrever o áudio
try:
    modelo_da_transcricao = whisper.load_model("small")
    transcricao = modelo_da_transcricao.transcribe(audio_do_video)
    texto_transcrito = transcricao["text"]
    print("Transcrição concluída:")
    print(texto_transcrito)

    # Apagar o arquivo de áudio
    os.remove(audio_do_video)
    print("Áudio deletado com sucesso.")
except Exception as e:
    print(f"Ocorreu um erro durante a transcrição: {e}")
    exit()

# Função para resumir o texto em tópicos
def summarize_text_in_topics(text):
    prompt = f"Resuma o seguinte texto no formato de tópicos:\n\n{text}\n\nResumo em tópicos:"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente que resume textos em tópicos."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Erro ao resumir o texto: {e}")
        return "Não foi possível gerar o resumo."

# Gerar resumo
resumo = summarize_text_in_topics(texto_transcrito)
print("Resumo em Tópicos:")
print(resumo)
