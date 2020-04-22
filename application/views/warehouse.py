from flask import Blueprint, render_template, session, redirect, request, url_for, flash
from flask import jsonify
from application.models import Product,Logistic
from application.extension import db
from application.views.block_publisher import add_block
import time
import os.path
import json
import base64
import io
import qrcode

warehouse_page = Blueprint("warehouse_page",__name__)

_basepath = os.path.abspath(os.path.dirname(__file__))

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

    # db.session.commit()
    #更新数据库的block_info
    status_rename = ["0","生产中状态","待运输状态","运输中状态","已到达状态","已入库状态"]
    # chain_index = int(product_status)-1
    logistics = Logistic.query.filter(Logistic.product_id == id).all()
    chain_index = 0
    pre_logistic = logistics[0]
    for log in logistics:
        if log.chain_index>chain_index:
            pre_logistic = log
            chain_index = log.chain_index
    chain_index += 1
    print(chain_index,pre_logistic)
    logistic = Logistic(product_status=product_status, product_id=id, product_number=product_num,
                        operator_id=session.get('user_id'), chain_index=chain_index)
    product_data = '商品名称: ' + product_name + '\n商品数量: ' + product_num + '\n商品状态: '+status_rename[int(product_status)]+ '\n商品描述: ' +\
                   product_description + '\n操作时间: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # pre_logistic = Logistic.query.filter(Logistic.product_id == id,Logistic.chain_index == (chain_index-1)).first()
    print(pre_logistic)
    pre_hash = pre_logistic.current_hash
    add_block(chain_index, product_data, pre_hash)
    block_path = _basepath + '\\pubBlock.txt'
    while not os.path.exists(block_path):
        print('waiting reply')
        time.sleep(1)
    with open(block_path, 'r', encoding='UTF-8') as f:
        print("Load str file from {}".format(block_path))
        logistic_info = json.load(f)
    os.remove(block_path)
    logistic.pre_hash = logistic_info['previous_hash']
    logistic.current_hash = logistic_info['now_hash']
    logistic.random_num = logistic_info['nonce']
    db.session.add(logistic)
    block_info = '\n\n区块编号: '+str(chain_index)+'\n商品ID: ' + str(id) + '\n操作者ID: '  + str(
        session.get('user_id')) + '\n'+ product_data + '\n上一区块hash: ' + logistic_info[
                     'previous_hash'] + '\n当前hash: ' + logistic_info['now_hash'] + '\n随机数: ' + str(
        logistic_info['nonce'])
    product.block_info += block_info
    #生成二维码
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=1,
    )
    qr.make(fit=True)
    qr.add_data(product.block_info)
    # print('qr_code的txt: ',block_info)
    img = qr.make_image()

    buf = io.BytesIO()
    img.save(buf, format='PNG')
    image_stream = buf.getvalue()
    heximage = base64.b64encode(image_stream)
    qr_code = 'data:image/png;base64,' + heximage.decode()
    # print(qr_code)
    product.qr_code = qr_code

    db.session.commit()
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
