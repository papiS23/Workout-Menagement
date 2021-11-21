from enum import unique
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    user_email = db.Column(db.String(30), unique=True)
    user_password = db.Column(db.String(60))

    def __init__(self, username, user_email, user_password):
        self.username = username
        self.user_email = user_email
        self.user_password = user_password

class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'username', 'user_email', 'user_password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route("/register", methods=['POST'])
def add_user():
    username = request.json['username']
    user_email = request.json['user_email']
    user_password = request.json['user_password']

    new_user = User(username, user_email, user_password)
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)


# @app.route("/allproducts", methods=['GET'])
# def get_products():
#     all_products = Product.query.all()
#     result = products_schema.dump(all_products)
#     return jsonify(result)


# @app.route("/product/<id>", methods=['GET'])
# def get_product(id):
#     product = Product.query.get(id)
#     return product_schema.jsonify(product)











if __name__ == '__main__':
    app.run(debug=True)