from flask import Blueprint
from src.controller.controller import (
    index,
    post,
    all_products
)

main = Blueprint('main', __name__)

main.add_url_rule("/", view_func=index, methods=["GET"])

main.add_url_rule("/allProducts", view_func=all_products, methods=["GET"])

main.add_url_rule("/post/", view_func=post, methods=["POST"], defaults={"parametro": None})
main.add_url_rule("/post/<parametro>", view_func=post, methods=["POST"])

def init_routes(app):
    app.register_blueprint(main)