import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()  # Carga el .env

def send_sales_email(subject, body, to_email=None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = os.getenv('MAIL_FROM')
    msg['To'] = to_email or os.getenv('MAIL_TO')
    msg.set_content(body)

    try:
        server = os.getenv('MAIL_SERVER')
        port = int(os.getenv('MAIL_PORT', 587))
        username = os.getenv('MAIL_USERNAME')
        password = os.getenv('MAIL_PASSWORD')
        use_tls = os.getenv('MAIL_USE_TLS', 'true').lower() == 'true'

        with smtplib.SMTP(server, port) as smtp:
            if use_tls:
                smtp.starttls()
            if username and password:
                smtp.login(username, password)

            smtp.send_message(msg)
            return True

    except Exception as e:
        print(f"Error enviando correo: {e}")
        return False
