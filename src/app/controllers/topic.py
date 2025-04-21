from flask import jsonify
from app.controllers.sales import handle_sales
from app.controllers.pricing import handle_pricing

def handle_topic_request(data):
    topic = data.get("topic")
    description = data.get("description")

    if not topic or not description:
        return jsonify({"error": "Faltan datos: 'topic' y 'description' son obligatorios"}), 400

    if topic == "sales":
        return handle_sales(description)

    if topic == "pricing":
        return handle_pricing(description)

    return jsonify({
        "error": f"Topic no válido: {topic}. Debe ser 'sales' o 'pricing'."
    }), 400
