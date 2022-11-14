from email import message
from flask import render_template,redirect,flash,session,abort,request,make_response,url_for,jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from pack import app,db,csrf
from pack.mymodels import Transaction
import datetime,os,random,string

Transaction = [

       {
        "customer_name" :"tolani giwa",
        "balance" :"13000",
       "customer_email": "Giwafauzziyyah@gmailcom",
       "pwd":"1234t",
       }
]

cus=Transaction["customer_name"]
bal=Transaction["13000"]
email=Transaction["customer_email"]
passw=Transaction["pwd"]


#REGISTRATION
@app.route("/transaction",methods=['POST','GET'])
@csrf.exempt
def registration():
    if request.method=='GET':
        return 'DONE'

    else:
        trans=db.session.execute(f"INSERT INTO transaction SET(customer_name={cus},balance={bal},customer_email={email},pwd={passw})")
        db.session.commit()
        return jsonify (trans)


@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('user/user_login.html')
    else:

        record=db.session.query(Transaction).all()
        if record and check_password_hash(record.pwd,record.pwd):
            userID=record.user_id
            session['loggedin']=userID
            return 'pass'
        else:
            msg='invalid login'
            flash(msg)
            return 'pass'

@app.route("/balance",methods=['GET'])
@csrf.exempt
def balance():
        trans=db.session.query(Transaction).filter(Transaction.customer_email==email,Transaction.balance==bal).first()

        return 'your balance is ...'


#LOGOUT
app.route("/logout")
def logout():
    if session.get('loggedin') !=None:
        session.pop('loggedin')
        return 'pass'

#DEPOSITE
@app.route("/update", methods=['POST','GET'])
def update():
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






