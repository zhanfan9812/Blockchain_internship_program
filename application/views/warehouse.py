from flask import Blueprint, render_template, session, redirect, request, url_for, flash
from flask import jsonify
from application.models import Product
from application.extension import db

warehouse_page = Blueprint("warehouse_page",__name__)

@warehouse_page.route("/getArriveCommList/<status>")
def getArriveCommList(status):
    #status = request.form.get("status")
    products = Product.query.filter(Product.status==status).all()
    data = []
    for product in products:
        product_data = {
            "id":product.id,
            "product_name":product.product_name,
            "status":product.status,
            "number":product.number,
            "date_of_pro":product.date_of_pro,
            "description":product.description
        }
        data.append(product_data)
    return jsonify({"data":data})

# @warehouse_page.route("/warehouse/updateStatus/<status>/<id>",methods=["get"])
# def wareHouseUpdateStatus(status,id):
#     product = Product.query.get(id)
#     product.status=status
#     db.session.commit()
#     return "1"

@warehouse_page.route("/warehouse/getInfo/<id>",methods=["POST"])
def commoditiesGetInfo(id):
    # print('id: ',id)
    product = Product.query.get(id)
    # print(product)
    product_data = {
        "id": product.id,
        "product_name": product.product_name,
        "status": product.status,
        "number": product.number,
        "date_of_pro": product.date_of_pro,
        "description": product.description
    }
    return jsonify({"product": product_data})

@warehouse_page.route("/warehouse/updateInfo/<id>",methods=["POST"])
def commoditiesUpdateInfo(id):
    id = request.form.get('id')
    product_name = request.form.get('product_name')
    product_num = request.form.get('product_num')
    product_description = request.form.get('product_description')
    product_status = request.form.get('product_status')

    if (product_name == "")| (product_num == ""):
        return '0_1'
    if Product.query.filter(Product.product_name == product_name, Product.id != id).first():
        return '0_2'

    product = Product.query.get(id)
    product.product_name = product_name
    product.status = product_status
    product.number = product_num
    product.description = product_description

    db.session.commit()
    #更新数据库的block_info
    return "1"


@warehouse_page.route("/warehouse/searchByCondition/<status>/<productId>")
def searchCommodityByCondition(status,productId):
    flag = productId.isdigit()
    if flag:
        product = Product.query.filter(Product.id==productId,Product.status==status).first()
    else:
        product = Product.query.filter(Product.product_name == productId,Product.status ==status).first()
    if  product is None:
        return ""
    else:
        product_data = {
            "id": product.id,
            "product_name": product.product_name,
            "status": product.status,
            "number": product.number,
            "date_of_pro": product.date_of_pro,
            "description": product.description
        }
        return jsonify({"product":product_data})

#得到总数据
@warehouse_page.route("/warehouse/getCount/<status>")
def getCount(status):
    count = Product.query.filter(Product.status==status).count()
    return str(count)

@warehouse_page.route("/warehouse/getProductsByPage/<status>/<curr>/<limit>")
def getProductsByPage(status,curr,limit):
    curr = int(curr)
    limit = int(limit)
    products = Product.query.filter(Product.status == status).offset((curr-1)*limit).limit(limit)
    data = []
    for product in products:
        product_data = {
            "id": product.id,
            "product_name": product.product_name,
            "status": product.status,
            "number": product.number,
            "date_of_pro": product.date_of_pro,
            "description": product.description
        }
        data.append(product_data)
    return jsonify({"data": data})

@warehouse_page.route("/product/getProductInfo/<id>",methods=['GET', 'post'])
def getProductInfo(id):
    id = int(id)
    product = Product.query.get(id)
    product_data = {
        "id": product.id,
        "product_name": product.product_name,
        "status": product.status,
        "number": product.number,
        "date_of_pro": product.date_of_pro,
        "description": product.description,
        "block_info":product.block_info,
        "qr_code":product.qr_code
    }
    return jsonify({"data" : product_data})
