from flask import  Blueprint, Response

products = Blueprint('products', __name__, url_prefix='/products')

@products.route('/<nombre>')
def get_products(nombre):
    if nombre == "pygroup":
        return Response("ERROR! No se puede usar el nombre pygroup",status=400)
    else:
        return Response("Felicitaciones! Trabajo exitoso {}".format(nombre),status=200)