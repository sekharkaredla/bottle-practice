from bottle import Bottle,request,run,route,template,static_file,response
import MySQLdb
app=Bottle()
db = MySQLdb.connect("localhost","root","pass","testdb")
cursor = db.cursor()

@app.route('/static/<filepath:path>')
def give_static_file(filepath):
    return static_file(filepath,root='static/')

@app.route('/')
def login():
    return template('login.html')

@app.route('/greet')
def check_login():
    if request.get_cookie('visit'):
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        return "hello again , you revisited ,,Database version : %s " % data
    else:
        return 'hello , you visited for the first time'
        response.set_cookie('visit','yes')

@app.route('/login',method='POST')
def login():
    if request.forms.get('uname')=='sekhar' and request.forms.get('pass')=='sekhar':
        return "<h1>SUCCESS</h1>"
    else:
        return "WRONG"

run(app,host='localhost',port='8888',debug=True)
