from flask import Blueprint, render_template

api = Blueprint('api',__name__, url_prefix='/api')
@api.route('/')
def getdata():
    return render_template('home.html')
    