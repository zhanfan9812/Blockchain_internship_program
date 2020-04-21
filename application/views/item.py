from flask import Blueprint, render_template, session, redirect, request,jsonify,url_for, flash
from application.models import Product,Logistic
from application.extension import db
from application.views.block_publisher import add_block
import time
import os.path
import json

producer_page = Blueprint('producer_page', __name__)

@producer_page.route('/producers/additem/<productNum>/<productName>/<productDescription>', methods=["POST"])
def additem(productNum,productName,productDescription):
    numFlag=productNum.isdigit()
    nameFlag=productName.isdigit()
    if nameFlag:
        return '0_1'
    if not numFlag:
        return '0_2'
    if Product.query.filter(Product.product_name == productName).first():
        return '0_3'
    item = Product(product_name=productName,status=1,number=productNum,description=productDescription)
    db.session.add(item)
    db.session.commit()
    product = Product.query.filter(Product.product_name == productName).first()
    product_id = product.id
    logistic = Logistic(product_status=1, product_id= product_id,product_number=productNum,operator_id=session.get('user_id'),chain_index=0)
    product_data = 'product_name: '+productName+'\nproduct_number: '+productNum+'\nproduct_status: 1'+'\nproduct_description: '+productDescription+'\nupdate_time: '+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    # print(product_data)
    add_block(0, product_data, '0')
    block_path='D:\\Github\\Blockchain_internship_program\\application\\views\pubBlock0.txt'
    while not os.path.exists(block_path):
        print('computing hash')
        time.sleep(1)
    with open(block_path, 'r') as f:
        print("Load str file from {}".format(block_path))
        logistic_info = json.load(f)
    os.remove(block_path)
    logistic.pre_hash = logistic_info['previous_hash']
    logistic.current_hash = logistic_info['now_hash']
    logistic.random_num = logistic_info['nonce']
    db.session.add(logistic)
    block_info = 'chain_index: 0\nproduct_id: '+str(product_id)+'\noperator_id: '+'\n'+str(session.get('user_id'))+product_data+'\nprevious_hash: '+logistic_info['previous_hash']+'\ncurrent_hash: '+logistic_info['now_hash']+'\nnonce: '+str(logistic_info['nonce'])
    product.block_info = block_info
    db.session.commit()
    return '1'


@producer_page.route('/producers/deleteitem', methods=["GET","POST"])
def deleteitem():
    id = request.form.get('productId')
    logistics=Logistic.query.filter(Logistic.product_id == id).all()
    # print(item)
    for logistic in logistics:
        db.session.delete(logistic)
    db.session.commit()
    item = Product.query.get(id)
    if(item is None):
        return "1"
    db.session.delete(item)
    db.session.commit()
    return "0"

@producer_page.route('/producer/edititem/<status>/<id>', methods=["GET"])
def producerUpdateStatus(status, id):
    # print(status)
    product = Product.query.get(id)
    product.status = status
    db.session.commit()
    return "1"

@producer_page.route('/producers/list', methods=["post"])
def list():
    products = Product.query.all()
    if products==None:
        return render_template('/all_commodities_list.html')
    # print('all products:',products)
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
    flag = name.isdigit()
    if flag:
        product = Product.query.filter(Product.id==name).first()
    else:
        product = Product.query.filter(Product.product_name == name).first()
    if product is None:
        return ""
    else:
        print(product)
        item_dict = {
            'id': product.id,
            'product_name': product.product_name,
            'number': product.number,
            'status': product.status,
            'date': product.date_of_pro,
            'description': product.description
        }
        return jsonify({"data": item_dict})

# @producer_page.route('/producers/list2', methods=["post"])
# def list2():
#     products = Product.query.filter(Product.status=='2').all()
#     if products is None:
#         return render_template('/comodities_needTransport.html')
#     print(products)
#     data=[]
#     for product in products:
#         item_dict = {
#         'id': product.id,
#         'product_name': product.product_name,
#         'number': product.number,
#         'status': product.status,
#         'date': product.date_of_pro,
#         'description': product.description
#     }
#         data.append(item_dict)
#     return jsonify({"data": data})
#
#
# @producer_page.route('/producers/searchbyid2', methods=["GET","POST"])
# def select_by_name2():
#     name=request.form.get('product_name')
#     products = Product.query.filter(Product.status == '2',Product.product_name==name).all()
#     print(products)
#     data=[]
#     for product in products:
#         item_dict = {
#         'id': product.id,
#         'product_name': product.product_name,
#         'number': product.number,
#         'status': product.status,
#         'date': product.date_of_pro,
#         'description': product.description
#     }
#         data.append(item_dict)
#     return jsonify({"data": data})

@producer_page.route('/producers/list3', methods=["post"])
def list3():
    # print('arrive list3')
    products = Product.query.filter(Product.status == 1).all()
    if products==None:
        return render_template('/commodities_making_list.html')
    # print(products)
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
    # print(name)
    flag = name.isdigit()
    if flag:
        product = Product.query.filter(Product.status == 1,Product.id==name).first()
    else:
        product = Product.query.filter(Product.status == 1,Product.product_name == name).first()
    if product is None:
        return ""
    else:
        # print(product)
        item_dict = {
            'id': product.id,
            'product_name': product.product_name,
            'number': product.number,
            'status': product.status,
            'date_of_pro': product.date_of_pro,
            'description': product.description
        }
        return jsonify({"product": item_dict})
    # name=request.form.get('product_name')
    # products = Product.query.filter(Product.status == 1, Product.product_name == name).all()
    # print(products)
    # data=[]
    # for product in products:
    #     item_dict = {
    #     'id': product.id,
    #     'product_name': product.product_name,
    #     'number': product.number,
    #     'status': product.status,
    #     'date': product.date_of_pro,
    #     'description': product.description
    # }
    #     data.append(item_dict)
    # return jsonify({"data": data})

# @producer_page.route('/producers/searchbyid', methods=["GET","POST"])
# def select_by_name():
#     name=request.form.get('product_name')
#     print(name)
#     flag = name.isdigit()
#     if flag:
#         product = Product.query.filter(Product.status == 1,Product.id==name).first()
#     else:
#         product = Product.query.filter(Product.status == 1,Product.product_name == name).first()
#     if product is None:
#         return ""
#     else:
#         print(product)
#         item_dict = {
#             'id': product.id,
#             'product_name': product.product_name,
#             'number': product.number,
#             'status': product.status,
#             'date': product.date_of_pro,
#             'description': product.description
#         }
#         return jsonify({"data": item_dict})

