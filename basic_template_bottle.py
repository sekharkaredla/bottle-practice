from bottle import route,run,Bottle,template,request
app=Bottle()

run(app,host ='localhost',port=7777,debug=True)
