from flask import Flask, jsonify, request, render_template
import requests
import mysql.connector
from datetime import datetime
from datetime import date
#from json2html import * 

'''db = mysql.connector.connect(
    host='localhost',
    user='pablo',
    passwd='admin',
    database="pruebas"
    )'''

#mycursor = db.cursor()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == 'POST'):
        if request.form.get("submit_a"):
			#status = request.page.get("onoff")
            #print(status)
    else:
        return render_template("page.html")

'''@app.route('/showtable', methods=['GET'])
def ShowTable():
    mycursor.execute("select * from data;")
    data = mycursor.fetchall()
    return render_template('mariadb.html', data=data)


@app.route('/jsontable', methods=['GET'])
def ShowTablePi():
    mycursor.execute("select * from data;")
    data = mycursor.fetchall()
    return jsonify(data)
'''

if (__name__ == '__main__'):
    app.run(host='0.0.0.0',port=8080)