
#importamos de la carpeta productos y del archivo models la variable products
from db import db, ma
from conf.config import DevelopmentConfig
from app.products.views import products

ACTIVE_ENDPOINTS = [('/products', products)]


def create_app(config=DevelopmentConfig):
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

    # register each active blueprint
    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)

    return app


if __name__ == "__main__":
    app_flask = create_app()
    app_flask.run()