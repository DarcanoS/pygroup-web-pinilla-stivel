import sys

from http import HTTPStatus
from flask import Blueprint, Response, request, render_template, redirect, url_for

from app.productos.forms import  CreateCategoryForm, Create_Stock_Form

from app.productos.models import get_all_categories, prueba, create_new_stock, \
    get_all_stock, create_new_category, create_new_product, get_all_products, \
        get_product_by_id, update_stock, delete_DB



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


@products.route('/categories',methods=['GET'])
def get_categories():
    """
    Retorna todas las categorias
    :return:
    """
    categories = get_all_categories()    

    if categories:
        RESPONSE_BODY["message"] = "OK. Categories List"
        RESPONSE_BODY["data"] = categories
        status_code = HTTPStatus.OK
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



@products.route('/', methods=['GET'])
def get_products():
    """
    retorna todos los productos
    :return:
    """
    products_obj = get_all_products()
    status_code = HTTPStatus.OK

    if products_obj:
        RESPONSE_BODY["message"] = "OK. Products List"
        RESPONSE_BODY["data"] = products_obj
        status_code = HTTPStatus.OK
    else:
        RESPONSE_BODY["message"] = "OK. No products found"
        RESPONSE_BODY["data"] = products_obj
        status_code = HTTPStatus.NOT_FOUND

    return RESPONSE_BODY, status_code

@products.route('/<int:numero>', methods=['GET'])
def get_product(numero):
    """
    retorna un producto por su id
    """
    product = get_product_by_id(numero)

    if product:
        RESPONSE_BODY["data"] = product
        status_code = HTTPStatus.OK
    else:
        RESPONSE_BODY["data"] = "Product Not Found"
        status_code = HTTPStatus.NOT_FOUND

    return RESPONSE_BODY, status_code

@products.route('/product-stock/<int:id>')
def get_product_stock(product_id):
    pass

@products.route('/stock', methods=['GET'])
def get_stock():
    """
    retorna todo el Stock
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

@products.route('/add-stock', methods=['PUT','POST'])
def create_stock():
    RESPONSE_BODY["message"] = "Method not allowed"
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    if request.method == "POST":
        data = request.json
        add_stock = create_new_stock(data["product_id"],data["quantity"])
        if add_stock:
            RESPONSE_BODY["message"] = "OK. Stock created!"
            RESPONSE_BODY["data"] = add_stock
            status_code = HTTPStatus.CREATED
        else:
            RESPONSE_BODY["message"] = "Stock Not Created"
            RESPONSE_BODY["data"] = add_stock
            status_code = HTTPStatus.BAD_REQUEST
    elif  request.method =="PUT":
        data = request.json
        add_stock = update_stock(data["id"],data["product_id"],data["quantity"])
        if add_stock:
            RESPONSE_BODY["message"] = "OK. Stock update!"
            RESPONSE_BODY["data"] = add_stock
            status_code = HTTPStatus.CREATED
        else:
            RESPONSE_BODY["message"] = "Stock Not Update"
            RESPONSE_BODY["data"] = add_stock
            status_code = HTTPStatus.NOT_FOUND

    return RESPONSE_BODY, status_code


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

@products.route('/delete')
def delete_stock():
    RESPONSE_BODY["data"] = delete_DB()
    return RESPONSE_BODY, 200

