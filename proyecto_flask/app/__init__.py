from flask import Flask, Response
from productos.models import products

app = Flask(__name__)



app.register_blueprint(products)

if __name__ == "__main__":
    app.run(debug=True)