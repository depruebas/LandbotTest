from flask import jsonify
import os
import logging
from datetime import datetime
from pythonjsonlogger import jsonlogger

os.makedirs("log", exist_ok=True)

# Configurar logger
logger = logging.getLogger("PricingLogger")
logger.setLevel(logging.INFO)

log_file = logging.FileHandler("log/pricing.json")
formatter = jsonlogger.JsonFormatter()
log_file.setFormatter(formatter)
logger.addHandler(log_file)

def handle_pricing(description):

    log_entry = {
        "topic": "pricing",
        "description": description,
        "date": datetime.utcnow().isoformat()
    }
    logger.info(log_entry)

    return jsonify({
        "status": "ok",
        "response": f"Ayuda sobre precios: {description}"
    })
