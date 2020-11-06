#Importamos el Blueprint y Response
from flask import  Blueprint, Response

#Creamos una variable tipo Blueprint, con el nombre 'products' y con la dirrecion de url '/products'
products = Blueprint('products', __name__, url_prefix='/products')

#creamos una sub-ruta. ej: 'http://127.0.0.1:5000/products/stivel' la variable nombre va a ser stivel
@products.route('/<nombre>')
def get_products(nombre):
    if nombre == "pygroup":
        #la funcion Response devuelve primero un estrin y despues una respuesta HTTP Response(String,HTTP)
        return Response("ERROR! No se puede usar el nombre pygroup",status=400)
    else:
        return Response("Felicitaciones! Trabajo exitoso {}".format(nombre),status=200)