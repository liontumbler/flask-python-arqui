from flask import jsonify
import requests
import logging

logging.basicConfig(
    filename='src/log/logs.log',
    level=logging.DEBUG,
    format='| %(asctime)s | %(levelname)s | %(message)s |'
)

dominio = 'https://fakestoreapi.com'
productos = '/products'

def get_products():
    return service(f"{dominio}{productos}")

def service(api):
    try:
        response = requests.get(api)
        logging.info(response)
        if response.status_code == 200:
            return response.json(), 200
        else:
            return jsonify({'error': 'Failed to fetch products'}), response.status_code
    except Exception as e:
        logging.error(str(e))
        return jsonify({'error': str(e)}), 500
