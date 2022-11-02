from cgitb import reset
from re import X
from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
from db import db
import datetime

dashboard_blueprint = Blueprint('dashboard_blueprint',__name__)

@dashboard_blueprint.route('/today-visitors')
def todayVisitors():

    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')
    sql = text('SELECT COUNT(id) AS today_visitors FROM visitors_log WHERE date = "'+currentDate+'"')
    result = db.engine.execute(sql)
    rawdata = result.fetchall()
    jsondata = jsonify([dict(row) for row in rawdata])
    return jsondata

@dashboard_blueprint.route('/overall-visitors')
def overallVisitors():

    sql = text('SELECT COUNT(id) AS overall_visitors FROM visitors_log')
    result = db.engine.execute(sql)
    rawdata = result.fetchall()
    jsondata = jsonify([dict(row) for row in rawdata])
    return jsondata


@dashboard_blueprint.route('/male-visitors')
def maleVisitors():

    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')
    sql = text('SELECT COUNT(id) AS male_visitors FROM visitors_log WHERE date = "'+currentDate+'" AND gender = 1')
    result = db.engine.execute(sql)
    rawdata = result.fetchall()
    jsondata = jsonify([dict(row) for row in rawdata])
    return jsondata


@dashboard_blueprint.route('/female-visitors')
def femaleVisitors():

    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')
    sql = text('SELECT COUNT(id) AS female_visitors FROM visitors_log WHERE date = "'+currentDate+'" AND gender = 2')
    result = db.engine.execute(sql)
    rawdata = result.fetchall()
    jsondata = jsonify([dict(row) for row in rawdata])
    return jsondata

@dashboard_blueprint.route('/table-data')
def tableData():

    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')
    x = ''

    for a in range(1,6):


        for g in range(1,3):


            #todays visitors
            currentDate = datetime.datetime.today().strftime('%Y-%m-%d')
            sql = text('SELECT COUNT(id) AS today_visitors FROM visitors_log WHERE date = "'+currentDate+'" AND gender = "'+str(g)+'" AND age_group ="'+str(a)+'"')
            result = db.engine.execute(sql)
            rawdata = result.fetchall()
            todayVisitors = rawdata[0].today_visitors

            # overall visitors
            sql = text('SELECT COUNT(id) AS overall_visitors FROM visitors_log WHERE gender = "'+str(g)+'" AND age_group ="'+str(a)+'"')
            result = db.engine.execute(sql)
            rawdata = result.fetchall()
            overallVisitors = rawdata[0].overall_visitors

            gText = ''
            aText = ''

            if(g == 1):
                gText = 'Male'
            elif(g == 2):
                gText = 'Female'

            if(a == 1):
                aText = 'Kids'
            elif(a == 2):
                aText = 'Teenagers'
            elif(a == 3):
                aText =  'Youngsters'
            elif(a == 4):
                aText =  'Adults'
            elif(a == 5):
                aText =  'Senior Citizen'

            x+= '("gender":"'+gText+'","age":"'+aText+'","todayVisitors":"'+str(todayVisitors)+'", "overallVisitors":"'+str(overallVisitors)+'"),'

    x = x[:-1]
    rawjson = '['+x+']'
    return rawjson

@dashboard_blueprint.route('/bargraph-data')
def bargraphdata():

    x = ''
    for m in range(1,13):

        sql = text('SELECT COUNT(id) AS month_visitors FROM visitors_log WHERE MONTH(data) ="'+str(m)+'"')
        result = db.engine.execute(sql)
        rawdata = result.fetchall()
        monthVisitors = rawdata[0].month_visitors
        x+= '{"month":"'+str(monthVisitors)+'"),'


    x=x[:-1]
    rawjson = '['+x+']'
    return rawjson