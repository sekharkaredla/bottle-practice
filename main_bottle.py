from bottle import route,Bottle,request,template,run
app=Bottle()
# @app.route('/')
# def index():
#     return '<h1>FIRST BOTTLE PAGE</h1>'

@app.route('/')
@app.route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)


@app.route('/show/<name:re:[a-z]+>')
def callback(name):
    return name

run(app,host='localhost',port='8888',debug=True)
