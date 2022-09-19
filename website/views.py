from flask import Flask,Blueprint,render_template,request,flash,redirect,url_for
from website import get_db
views = Blueprint('views',__name__)
app= Flask(__name__)

@views.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST" and 'query' in request.form:
        query = request.form['query']
        return redirect(url_for('.results',query=query))
    return render_template("index.html") 

@views.route('/categories',methods=['GET','POST'])
def categories():
    if request.method == "POST" and 'query' in request.form:
        query = request.form['query']
        return redirect(url_for('.results',query=query))
    return render_template("categories.html")

@views.route('/results',methods=['POST','GET'])
def results():
    if request.method == "GET":
        return redirect(url_for(".home",))
    else:
        query = request.form['query']
        conn=get_db()
        cursor = conn.cursor()
        cursor.execute("select * from charity_list")
        conn.commit()
        result= "<h1>charityname</h1><br>"
        
        return render_template("results.html",query=query,result=result,conn=conn)