from flask import Flask, jsonify, request, render_template
import requests
import mysql.connector
from datetime import datetime
from datetime import date
#from json2html import * 

db = mysql.connector.connect(
    host='localhost',
    user='pablo',
    passwd='admin',
    database="pruebas"
    ) 

mycursor = db.cursor()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == 'POST'):
        tempJson = request.get_json()
        print(tempJson) 
        if (tempJson['20'] == '1'):
            now = datetime.now().strftime("%H:%M:%S") 
            dateD = str(date.today())
            print(dateD) 
            mycursor.execute("insert into data values (default,'{}','{}','on')".format(dateD,now))
            db.commit()
            return jsonify({'21':'True'}), 201
        else:
            now = datetime.now().strftime("%H:%M:%S")
            dateD = str(date.today())
            print(dateD)
            mycursor.execute("insert into data values (default,'{}','{}','on')".format(dateD,now))
            db.commit()
            return jsonify({'21':'False'}), 201
    else:
        return jsonify({'about':'Hola Pablo'})


@app.route('/showtable', methods=['GET'])
def ShowTable():
    mycursor.execute("select * from data;")
    data = mycursor.fetchall()
    return render_template('mariadb.html', data=data)


@app.route('/jsontable', methods=['GET'])
def ShowTablePi():
    mycursor.execute("select * from data;")
    data = mycursor.fetchall()
    return jsonify(data)


if (__name__ == '__main__'):
    app.run(host='0.0.0.0',port=8080)