from datetime import datetime

from flask import jsonify

from app.db import db, ma


class Product(db.Model):
    """
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(500), default="https://bit.ly/3loPYXP")
    price = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, default=1)
    description = db.Column(db.String(500), nullable=True)
    refundable = db.Column(db.Boolean, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        #fields = ["id", "name", "price"]


class Category(db.Model):
    """
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category


class Stock(db.Model):
    """
    """
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

class StockSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Stock



def get_all_categories():
    categories = Category.query.all()
    category_schema = CategorySchema()
    categories = [category_schema.dump(category) for category in categories]
    return categories


def create_new_category(name):
    category = Category(name=name)
    db.session.add(category)

    if db.session.commit():
        return category

    return None


def create_new_product(name,price,refundable):
    new_product = Product(name=name,price=price,refundable=refundable)
    db.session.add(new_product)

    if db.session.commit():
        return new_product

    return None


def get_all_products():
    products_qs = Product.query.all()
    product_schema = ProductSchema()
    products_serialization = [product_schema.dump(product) for product in
                              products_qs]

    return products_serialization


def get_product_by_id(id):
    product_qs = Product.query.filter_by(id=id).first()
    product_schema = ProductSchema()
    p = product_schema.dump(product_qs)

    return p

def get_all_stock():
    get_stock = Stock.query.all()
    stock_schema = StockSchema()
    get_stock = [stock_schema.dump(stock) for stock in get_stock]
    return get_stock

def create_new_stock(product_id, quantity):
    product_qs = Product.query.filter_by(id=product_id).first()
    product_schema = ProductSchema()
    p = product_schema.dump(product_qs)
    if p:
        new_stock = Stock(product_id=product_id,quantity=quantity)
        db.session.add(new_stock)
        db.session.commit()
        
        return StockSchema().dump(new_stock)
    
    return None


def update_stock(id,product_id, quantity):
    stock_schema = StockSchema()
    stock_in_DB = stock_schema.dump(Stock.query.filter_by(id=id).first())
    if stock_in_DB:
        db.session.query(Stock).filter_by(id=id).update({"quantity":quantity})
        update = db.session.commit()
        
        stock_in_DB = stock_schema.dump(Stock.query.filter_by(id=id).first())
        
        return stock_in_DB
    return None



