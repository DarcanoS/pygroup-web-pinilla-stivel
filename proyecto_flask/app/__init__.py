from flask import Flask, Response
#importamos de la carpeta productos y del archivo models la variable products
from productos.models import products

app = Flask(__name__)


#inicializamos la variable products que es tipo Blueprint
app.register_blueprint(products)

#esto no se que hace, pero se debe colocar :'v
if __name__ == "__main__":
    app.run(debug=True)