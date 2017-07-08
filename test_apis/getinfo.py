from flask import jsonify ,request
from ..  import db
from ..models import User
from . import api
import json

@api.route('/getinfo/<int:id>/', methods=['GET'])
def get_info(id):
    if request.method == 'GET':
        user = User.query.get_or_404(id)
        name = user.username
        time = user.time
        owner_id = user.id
        forgive_time = user.forgive_time
        return jsonify({
                        "name":name,
                        "time":time,
                        "owner_id":owner_id,
                        "forgive_time":forgive_time
                        })
