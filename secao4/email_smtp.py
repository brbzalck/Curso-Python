import os # Acessa arquivos/caminhos no pc
import pathlib # Acesso em diretórios
import smtplib # Configura servidor smtp
from email.mime.multipart import MIMEMultipart # Define informações essênciais(de qm, para qm, assunto)
from email.mime.text import MIMEText # Adiciona texto no email
from string import Template # Troca dados de determinado arquivo
from dotenv import load_dotenv # Carrega env

load_dotenv() # Carregando o .env 


CAMINHO_HTML = pathlib.Path(__file__).parent / 'email.html'

# Dados do remetente e destinatário(estou enviando um email para mim mesmo)
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# Configuração SMTP - Configurando conexão com servidor do Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = os.getenv('FROM_EMAIL', '') # Definindo email em usuário
smtp_password = os.getenv('EMAIL_PASSWORD', '') # Definindo senha armazenada no meu .env(variável de ambiente)

# Mensagem de texto
with open(CAMINHO_HTML, 'r') as arquivo:
    texto_arquivo = arquivo.read() # Lendo o arquivo e armazenando numa VAR
    template = Template(texto_arquivo) # Usando a classe Template(argumento=texto_arquivo) (self=template)
    texto_email = template.substitute(nome='Lucas')

# Transformar nossa mensagem em MIMEMultipart - Especificando Remetente Destinatário e Assunto
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Você está evoluindo na computaria dog.'

# Inserindo meu texto Com formato.html e Estilo-utf-8
corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Iniciando conexão com servidor
with smtplib.SMTP(smtp_server, smtp_port) as server: # Definindo qual server vou utilizar
    server.ehlo()
    server.starttls() # Iniciando conexão segura
    server.login(smtp_user, smtp_password) # Logando com as informações do meu .env
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso.')

