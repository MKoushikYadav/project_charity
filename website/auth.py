
from flask import Blueprint,render_template,request,flash,redirect,url_for
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    print(request.form)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return"<p>logout</p>"

@auth.route("signup",methods=['GET','POST'])
def signup():
    if request.method == 'POST':
            return redirect(url_for('views.home'))
    return render_template('sign_up.html')