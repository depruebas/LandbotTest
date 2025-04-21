from flask import jsonify

def handle_pricing(description):

    # Send to slack channel
    return jsonify({
        "status": "ok",
        "response": f"Ayuda sobre precios: {description}"
    })
