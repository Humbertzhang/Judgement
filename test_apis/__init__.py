from flask import Blueprint

api = Blueprint('api',__name__)

from . import signup,signin,getinfo,uploadtime,forgive
