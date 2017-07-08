from . import api
from .. import db
from flask import request
from flask import jsonify
from ..models import User

@api.route('/signup/', methods=['POST'])
def signup():
    if request.method == 'POST':

        un = request.get_json().get('username')
        passwd = request.get_json().get('password')
        #email = request.get_json().get('email')
        
        user = User.query.filter_by(username=un).first()

        if user:
            return jsonify({}), 400
    
        new_user = User(
                        username=un,
                        password=passwd,
                        time=0
                       )
#        new_user.password(passwd)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'created': new_user.id}), 200
