import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Olá! Esse é um e-mail automático enviado pelo Python.")
msg["Subject"] = "Teste de E-mail"
msg["From"] = "seuemail@gmail.com"
msg["To"] = "destinatario@gmail.com"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login("seuemail@gmail.com", "sua_senha")
    server.send_message(msg)

print("E-mail enviado!")
