from email import message
from flask import render_template,redirect,flash,session,abort,request,make_response,url_for,jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from pack import app,db,csrf
from pack.mymodels import Transaction
import datetime,os,random,string

Transaction = [

        {"customer_name": "tolani giwa"},
        {"balance": "13000"},
        {"customer_email": "Giwafauzziyyah@gmailcom"},
        {"pwd": "1234t"},

]


#REGISTRATION
@app.route("/transaction",methods=['POST','GET'])
def registration():
    if request.method=='GET':
        return 'DONE'

    else:
        trans=db.session.execute( f"INSERT INT0 transaction VALUES(customer_name=Transaction["customer_name"], balance=Transaction["balance"], customer_email=Transaction["customer_email"],) ")
        db.session.commit()
        return 'succesfully register'


@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('user/user_login.html')
    else:

        record=db.session.execute(f"SELECT * FROM transaction")
        if record and check_password_hash(record.pwd,record.pwd):
            userID=record.user_id
            session['loggedin']=userID
            return 'pass'
        else:
            msg='invalid login'
            flash(msg)
            return 'pass'



#LOGOUT
app.route("/logout")
def logout():
    if session.get('loggedin') !=None:
        session.pop('loggedin')
        return 'pass'

#DEPOSITE
@app.route("/update", methods=['POST','GET'])
def doctor_update():
    if session.get('loggedin') !=None:
        if request.method=='GET':
            trans= db.session.query(Transaction).all()
            return "pass"
        else:

            depositee=130000

            made_deposite=db.session.query(Transaction).filter(trans_id=session.get('loggedin')).first()
            made_deposite.deposite=depositee
            db.session.commit()
            return 'pass'

    else:
        return 'pass'






