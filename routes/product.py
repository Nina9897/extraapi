from flask import Blueprint, jsonify, request
from controllers.productController import get_all_products, get_product_by_id, create_product, edit_product, delete_product

product_bp = Blueprint('products', __name__)

@product_bp.route('/', methods=['GET'])
def index():
    products = get_all_products()
    return jsonify(products)

@product_bp.route('/<id>', methods=['GET'])
def get_product(id):
    return get_product_by_id(id)

@product_bp.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    new = create_product(name, description, price)
    return jsonify(new)

@product_bp.route('/edit/<id>', methods=['POST'])
def edit(id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    return edit_product(id, name, description, price)

@product_bp.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    return delete_product(id)
