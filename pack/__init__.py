from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
app=Flask(__name__,instance_relative_config=True)
app.config.from_pyfile('config.py')
db=SQLAlchemy(app)
csrf=CSRFProtect(app)
from pack import mymodels
from pack.routes import api_routes,user_routes