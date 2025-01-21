# Analisando vídeos
Este programa recolhe uma URL do youtube, transcreve o audio, e assim resumindo o vídeo  usando a IA da OpenIA. Tendo um auto desempenho e agilidade.

# Tecnologias
- Python
- openai
- whisper
- os
- re
- yt_dlp
- dotenv
# PRÉ REQUISTOS
1) Instale Python3 (https://www.python.org/downloads/)
![image](https://github.com/user-attachments/assets/0ded5cf5-4d7d-4fe6-96ca-42eee8fce90e)
2) Configure sua API da OpenIA (https://openai.com/index/openai-api/)
![image](https://github.com/user-attachments/assets/c57dd6e1-3e0d-46f7-b656-57b3c0ae512d)
- Crie o logue em uma conta
- Salve a Key da sua API (No arquivo .env)
3) Instale as dependências:
PARA INSTALAMENTO GERAL USE:
````pip install -r requirements.txt````
As dependências necessárias para o funcionamento do código são:
openai: Para mostrar notificações no Windows.
  - Instalação: ````pip install openai````
whisper: Para manipulação de dados em formato de tabela (DataFrame).
  - Instalação: ````pip install whisper````
selenium: Para automação de navegadores, utilizado para interação com sites.
  - Instalação: ````from yt_dlp install YoutubeDL ````
dotenv: Para ler e escrever arquivos Excel (.xlsx).
  - Instalação: ````from dotenv import load_dotenv````
os e re: Geralmente já está incluído com a instalação padrão do Python.
Além disso, o código utiliza módulos internos do Python, como ````os```` e ````re````.
# Se o vídeo for mais de 30min considere dividir-lo em partes para que consiga melhor funcionamento e
De uma olhada na base do modelo whisper ````modelo_da_transcricao = whisper.load_model("small")````
![image](https://github.com/user-attachments/assets/d4bd9e8c-ca5a-4591-994a-4f857ed004dd)

(https://github.com/openai/whisper)

# Lembre-se a API da OpenIA é paga, então faça uma recarga no mínimo de $5 para conseguir fazer os resumos (https://platform.openai.com/settings/organization/billing/overview)
![image](https://github.com/user-attachments/assets/f30aeff2-3b15-46a2-94c1-037ba5743031)
