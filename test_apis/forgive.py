from flask import jsonify,request
from .. import db
from ..models import User
from . import api
import json

@api.route('/forgive/',methods=['POST'])
def forgive():
    if request.method == 'POST':
        my_id = int(request.get_json().get('my_id'))
        user = User.query.filter_by(id = my_id).first()
        if(user.forgive_time>=1):
            user.forgive_time-=1
        elif(user.forgive_time==0):
            pass
        db.session.add(user)
        db.session.commit()

        return jsonify({
            'forgive_time':user.forgive_time
            })

