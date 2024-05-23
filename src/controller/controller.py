from flask import request, jsonify
from src.services.services import (
    get_products
)

def index():
    return "edwin"

def all_products():
    res = get_products()
    return res

def post(parametro):
    print(request)
    print(parametro)
    return 'parametro'