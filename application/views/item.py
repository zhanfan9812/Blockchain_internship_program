from flask import Blueprint, render_template, session, redirect, request,jsonify,url_for, flash
from application.models import Product,Logistic
from application.extension import db
import time
import json

producer_page = Blueprint('producer_page', __name__)

@producer_page.route('/producers/additem/<productNum>/<productName>/<productDescription>', methods=["get"])
def additem(productNum,productName,productDescription):
   # name=session.get('user_name')
    print(productNum)
    item_id=Product.query.count()+1
    product_name = productName
    Status=1
    Number=productNum
    date_of_produce=time.gmtime()
    text=productDescription
    item=Product(id=item_id,product_name=product_name,status=Status,number=Number,date=date_of_produce,description=text)
    db.session.add(item)
    db.session.commit()
    return "1"


@producer_page.route('/producers/deleteitem', methods=["GET","POST"])
def deleteitem():
    id = request.form.get('productId')
    item=Product.query.get(id)
    print(item)
    if(item is None):
        return "1"
    db.session.delete(item)
    db.session.commit()
    return "0"

@producer_page.route('/producer/edititem/<status>/<id>', methods=["GET"])
def producerUpdateStatus(status, id):
    print(id)
    product = Product.query.get(id)
    product.status = status
    db.session.commit()
    return "1"

@producer_page.route('/producers/list', methods=["post"])
def list():
    products = Product.query.all()
    if products==None:
        return render_template('/all_commodities_list.html')
    print(products)
    data=[]
    for product in products:
        item_dict = {
        'id': product.id,
        'product_name': product.product_name,
        'number': product.number,
        'status': product.status,
        'date': product.date_of_pro,
        'description': product.description
    }
        data.append(item_dict)
    return jsonify({"data": data})


@producer_page.route('/producers/searchbyid', methods=["GET","POST"])
def select_by_name():
    name=request.form.get('product_name')
    products = Product.query.filter(Product.product_name==name)
    print(products)
    data=[]
    for product in products:
        item_dict = {
        'id': product.id,
        'product_name': product.product_name,
        'number': product.number,
        'status': product.status,
        'date': product.date_of_pro,
        'description': product.description
    }
        data.append(item_dict)
    return jsonify({"data": data})

@producer_page.route('/producers/list2', methods=["post"])
def list2():
    products = Product.query.filter(Product.status=='2').all()
    if products is None:
        return render_template('/comodities_needTransport.html')
    print(products)
    data=[]
    for product in products:
        item_dict = {
        'id': product.id,
        'product_name': product.product_name,
        'number': product.number,
        'status': product.status,
        'date': product.date_of_pro,
        'description': product.description
    }
        data.append(item_dict)
    return jsonify({"data": data})


@producer_page.route('/producers/searchbyid2', methods=["GET","POST"])
def select_by_name2():
    name=request.form.get('product_name')
    products = Product.query.filter(Product.status == '2',Product.product_name==name).all()
    print(products)
    data=[]
    for product in products:
        item_dict = {
        'id': product.id,
        'product_name': product.product_name,
        'number': product.number,
        'status': product.status,
        'date': product.date_of_pro,
        'description': product.description
    }
        data.append(item_dict)
    return jsonify({"data": data})

@producer_page.route('/producers/list3', methods=["post"])
def list3():
    products = Product.query.filter(Product.status == 1).all()
    if products==None:
        return render_template('/commodities_making_list.html')
    print(products)
    data=[]
    for product in products:
        item_dict = {
        'id': product.id,
        'product_name': product.product_name,
        'number': product.number,
        'status': product.status,
        'date': product.date_of_pro,
        'description': product.description
    }
        data.append(item_dict)
    return jsonify({"data": data})


@producer_page.route('/producers/searchbyid3', methods=["post"])
def select_by_name3():
    name=request.form.get('product_name')
    products = Product.query.filter(Product.status == 1, Product.product_name == name).all()
    print(products)
    data=[]
    for product in products:
        item_dict = {
        'id': product.id,
        'product_name': product.product_name,
        'number': product.number,
        'status': product.status,
        'date': product.date_of_pro,
        'description': product.description
    }
        data.append(item_dict)
    return jsonify({"data": data})

