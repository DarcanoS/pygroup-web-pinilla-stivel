"""
render_template de Flask:
Flask utiliza por defecto jinja2 para generar documentos HTML, para generar una plantilla utilizamos la función render_template que recibe como parámetro el fichero donde guardamos la plantilla y las variables que se pasan a esta.
Las plantillas las vamos a guardar en ficheros en el directorio templates (dentro del directorio aplicacion).
"""

from http import HTTPStatus
from flask import Blueprint, Response, request, render_template, redirect, url_for

from app.productos.forms import  CreateCategoryForm

from app.productos.models import get_all_categories, prueba, create_new_stock, get_all_stock, create_new_category, create_new_product, get_all_products, get_product_by_id



products = Blueprint("products", __name__, url_prefix='/products')

EMPTY_SHELVE_TEXT = "Empty shelve!"
PRODUCTS_TITLE = "<h1> Products </h1>"
DUMMY_TEXT = "Dummy method to show how Response works"
RESPONSE_BODY = {
    "message": "",
    "data": [],
    "errors": [],
    "metadata": []
}


@products.route('/dummy-product', methods=['GET', 'POST'])
def dummy_product():
    """ This method test the request types. If is GET Type it will
    render the text Products in h1 label with code 500.
    If is POST Type it will return Empty shelve! with status code 403
    """
    if request.method == 'POST':
        return EMPTY_SHELVE_TEXT, HTTPStatus.FORBIDDEN

    return PRODUCTS_TITLE, HTTPStatus.INTERNAL_SERVER_ERROR


@products.route('/dummy-product-2')
def dummy_product_two():
    """ This method shows how Response object could be used to make API
    methods.
    """
    return Response(DUMMY_TEXT, status=HTTPStatus.OK)


@products.route('/categories')
def get_categories():
    """
        Verificar que si get_all_categories es [] 400, message = "No hay nada"
    :return:
    """
    categories = get_all_categories()
    status_code = HTTPStatus.OK

    if categories:
        RESPONSE_BODY["message"] = "OK. Categories List"
        RESPONSE_BODY["data"] = categories
    else:
        RESPONSE_BODY["message"] = "OK. No categories found"
        RESPONSE_BODY["data"] = categories
        status_code = HTTPStatus.NOT_FOUND

    return RESPONSE_BODY, status_code


@products.route('/add-category', methods=['POST'])
def create_category():
    """
    :return:
    """
    RESPONSE_BODY["message"] = "Method not allowed"
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    if request.method == "POST":
        data = request.json
        category = create_new_category(data["name"])
        RESPONSE_BODY["message"] = "OK. Category created!"
        RESPONSE_BODY["data"] = category
        status_code = HTTPStatus.CREATED

    return RESPONSE_BODY, status_code



@products.route('/add-product', methods=['POST'])
def create_product():
    

    RESPONSE_BODY["message"] = "Method not allowed"
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    if request.method == "POST":
        data = request.json
        add_product = create_new_product(data["name"],data["price"],data["refundable"])
        RESPONSE_BODY["message"] = "OK. Product created!"
        RESPONSE_BODY["data"] = add_product
        status_code = HTTPStatus.CREATED

    return RESPONSE_BODY, status_code



@products.route('/')
def get_products():
    products_obj = get_all_products()
    status_code = HTTPStatus.OK

    if products_obj:
        RESPONSE_BODY["message"] = "OK. Products List"
        RESPONSE_BODY["data"] = products_obj
    else:
        RESPONSE_BODY["message"] = "OK. No products found"
        RESPONSE_BODY["data"] = products_obj
        status_code = HTTPStatus.NOT_FOUND

    return RESPONSE_BODY, status_code


@products.route('/product/<int:id>')
def get_product(id):
    product = get_product_by_id(id)

    RESPONSE_BODY["data"] = product
    return RESPONSE_BODY, 200


@products.route('/product-stock/<int:id>')
def get_product_stock(product_id):
    pass

@products.route('/stock')
def get_stock():
    """
        Verificar que si get_all_categories es [] 400, message = "No hay nada"
    :return:
    """
    get_stock = get_all_stock()
    status_code = HTTPStatus.OK

    if get_stock:
        RESPONSE_BODY["message"] = "OK. Categories List"
        RESPONSE_BODY["data"] = get_stock
    else:
        RESPONSE_BODY["message"] = "OK. No Stock found"
        RESPONSE_BODY["data"] = get_stock
        status_code = HTTPStatus.NOT_FOUND

    return RESPONSE_BODY, status_code

@products.route('/add-stock', methods=['POST'])
def create_stock():
    

    RESPONSE_BODY["message"] = "Method not allowed"
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    if request.method == "POST":
        data = request.json
        add_stock = create_new_stock(data["product_id"],data["quantity"])
        RESPONSE_BODY["message"] = "OK. Stock created!"
        RESPONSE_BODY["data"] = add_stock
        status_code = HTTPStatus.CREATED

    return RESPONSE_BODY, status_code


@products.route('/need-restock')
def get_products_that_need_restock():
    pass


@products.route('/register-product-stock/<int:id>', methods=['PUT', 'POST'])
def register_product_refund_in_stock():
    pass

@products.route('/prueba/<numero>', methods=['GET'])
def prueba_mia(numero):
     RESPONSE_BODY["data"]= prueba(numero)
     return RESPONSE_BODY

@products.route('/success')
def success():
    return render_template('category_success.html')

@products.route('/create-category-form', methods=['GET', 'POST'])
def create_category_form():
    form_category = CreateCategoryForm()
    if request.method == 'POST' and form_category.validate():
        create_new_category(name=form_category.name.data)
        return redirect(url_for('products.success'))


    return render_template('create_category_form.html', form=form_category)