#-*- coding: utf-8 -*-
from flask import jsonify ,request
from ..  import db
from ..models import User
from . import api

@api.route('/signin/',methods=['GET','POST'])
def login():
    un = request.get_json().get("username")
    passwd = request.get_json().get("password")
    
    user = User.query.filter_by(username=un).first()
    if not user:
        return jsonify({}), 403
    if user is not None and user.verify_password(passwd):
        token = user.generate_auth_token()
        return jsonify ({
                        "id" : user.id,
                        "token" : token,
                        }), 200
    #else:
    #    return jsonify({}), 502
