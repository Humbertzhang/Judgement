from flask import jsonify ,request
from ..  import db
from ..models import User
from . import api
import json


@api.route('/uploadtime/<int:id>/', methods=['PUT'])
def upload_time(id):
    if request.method == 'PUT':
        
        my_id = int(request.get_json().get('my_id'))
        time = float(request.get_json().get('time'))
        user = User.query.filter_by(id=my_id).first()
        user.time = time
        db.session.add(user)
        db.session.commit()

        return jsonify({
            'status':200
        })
