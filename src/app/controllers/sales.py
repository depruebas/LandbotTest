from flask import jsonify
from app.utils.mailer import send_sales_email
import os

def handle_sales(description):
    # Lógica del topic "sales"
    subject = "Nueva solicitud de ayuda sobre ventas"
    body = f"Descripción enviada: {description}"

    email_sent = send_sales_email(subject, body)

    return jsonify({
        "status": "ok",
        "email_sent": email_sent,
        "response": "Ayuda sobre ventas recibida y correo enviado."
    })
