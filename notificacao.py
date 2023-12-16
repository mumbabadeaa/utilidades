# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def enviar_email(destinatario, assunto, corpo, anexo=None):
    # Configurações do servidor de e-mail
    email_rem = "lojawantonn@gmail.com"
    senha_rem = "nyeratitebkhanhp"
    servidor_smtp = "smtp.gmail.com"
    porta_smtp = 587

    # Construindo a mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = email_rem
    msg['To'] = destinatario
    msg['Subject'] = assunto
    # Adicionando o corpo do e-mail
    msg.attach(MIMEText(corpo, 'plain'))
    # Adicionando anexo, se houver
    if anexo:
        with open(anexo, 'rb') as arquivo:
            part = MIMEApplication(arquivo.read())
        part.add_header('Content-Disposition', 'attachment', filename=anexo)
        msg.attach(part)
    # Conectando ao servidor de e-mail e enviando a mensagem
    try:
        server = smtplib.SMTP(servidor_smtp, porta_smtp)
        server.starttls()  # Inicia a conexão segura
        server.login(email_rem, senha_rem)
        server.sendmail(email_rem, destinatario, msg.as_string())
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print("Ocorreu um erro ao enviar o e-mail:", str(e))
    finally:
        server.quit()
