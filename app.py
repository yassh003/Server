from flask import Flask
from db import db
from flask_cors import CORS
from visitorlog import visitor_blueprint
from dashboard import dashboard_blueprint
app = Flask(__name__)
CORS(app)

#db config
username = 'root'
password = ''
userpass = 'mysql+pymysql://'+username+':'+password+'@'
server = '127.0.0.1'
dbname = '/wallmart_visitor_log'
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
#register blueprint
app.register_blueprint(visitor_blueprint)
app.register_blueprint(dashboard_blueprint)

@app.route('/')
def firstScript():
    return "Server is up and running"


if __name__ == '__main__':
    app.debug = True
    app.run()