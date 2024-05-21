from flask import request, jsonify
import logging

#from src.services.services import ()

logging.basicConfig(
    filename='src/log/logs.log',
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

def index():
    return "edwin"

def post(parametro):
    #logging.info(request.args)

    status = 500
    if parametro is None:
        response = {
            "message": "Creando datos sin parámetro",
            "status": "success"
        } 
        status = 405
    else:
        response = {
            "message": f"Creando datos para {parametro}",
            "status": "success"
        }
        status = 200

    return jsonify(response), status