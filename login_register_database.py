from bottle import Bottle,response,request,run,template,static_file
import MySQLdb
app=Bottle()
db = MySQLdb.connect('localhost','root','pass','sek091')
cursor = db.cursor()

@app.route('/static/<filepath:path>')
def get_static_file(filepath):
    return static_file(filepath,root='static/')

@app.route('/')
def index():
    return template('login.html')

@app.route('/login',method='POST')
def login_details():
    user=request.forms.get('uname')
    sql='SELECT password FROM CREDENTIALS WHERE username="%s"'%(user)
    cursor.execute(sql)
    result=cursor.fetchone()
    if result[0]==request.forms.get('pass'):
        return template('success.html',name=user)
    else:
        return "<h1>WRONG</h1>"

@app.route('/register',method='POST')
def show_register_page():
    return template('register.html')

@app.route('/new_register',method='POST')
def register_details():
    user=request.forms.get('uname')
    try:
        sql='INSERT INTO CREDENTIALS (username,password) VALUES("%s","%s")'%\
                        (user,request.forms.get('pass'))
        cursor.execute(sql)
        db.commit()
        return template('success.html',name=user)
    except Exception as e:
        db.rollback()
        return "<h1>SOME ERROR OCCURED WITH DATABASE</h1> "+str(e)
run(app,host='localhost',port='8888',debug=True)
