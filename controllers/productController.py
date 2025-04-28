from models.product import Product
from config import db
from flask import jsonify

def get_all_products():
    try:
        return [product.to_dict() for product in Product.query.all()]
    except Exception as e:
        return jsonify({"error": str(e)})

def get_product_by_id(id):
    try:
        product = Product.query.get(id)
        if product:
            return product.to_dict()
        else:
            return jsonify({"error": "Producto no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_product(name, description, price):
    try:
        new_product = Product(name, description, price)
        db.session.add(new_product)
        db.session.commit()
        return new_product.to_dict()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)})

def edit_product(id, name, description, price):
    product = Product.query.get(id)
    if not product:
        return jsonify({"error": "El producto no existe"})
    
    product.name = name
    product.description = description
    product.price = price
    try:
        db.session.commit()
        return jsonify({"message": "Producto modificado"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Error modificando el producto: {str(e)}"})

def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"error": "El producto no existe"})
    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Producto eliminado"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Error eliminando el producto: {str(e)}"})
