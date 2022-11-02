from flask import Blueprint,request
from sqlalchemy.sql import text
from db import db
import datetime

visitor_blueprint = Blueprint('visitor_blueprint',__name__)

@visitor_blueprint.route('/add-visitors',methods=['POST'])
def adVisitors():

    gender = request.form['gender']
    age_group = request.form['age-group']
    comments = request.form['comments']
    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')

    sql = text('INSERT INTO visitors_log (gender,age_group,comments,date) VALUES ("'+gender+'","'+age_group+'","'+comments+'","'+currentDate+'")')
    db.engine.execute(sql)

    return "Data logged successfully"
