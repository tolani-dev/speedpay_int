import datetime
from pack import db


class Transaction(db.Model): 
    trans_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    customer_name = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Integer(), nullable=False)
    customer_email = db.Column(db.String(255), nullable=False)
    pwd = db.Column(db.String(255), nullable=False)
    deposit = db.Column(db.Integer(), nullable=False)

