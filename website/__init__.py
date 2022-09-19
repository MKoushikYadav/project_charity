from flask import Flask,render_template,g,request
import pymysql
#from os import path
app = Flask(__name__)

def connect_db():
    '''Connect to database'''
    return pymysql.connect(host="localhost", user="root",password="Manukayadav.15022", database="charity")


def get_db():
    '''Opens a new database connection per request and connects to app.g'''        
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db 

@app.teardown_appcontext
def close_db(error):
    '''Closes the database connection at the end of request.'''    
    if hasattr(g, 'db'):
        g.db.close()  


def create_app():
    '''Creates app'''
    from .auth import auth
    from .views import views
    #from .config import config
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
     
    return app

