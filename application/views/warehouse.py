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

@warehouse_page.route("/warehouse/updateStatus/<status>/<id>",methods=["get"])
def wareHouseUpdateStatus(status,id):
    product = Product.query.get(id)
    product.status=status
    db.session.commit()
    return "1"

