from flask import Flask, redirect, url_for, jsonify, request, render_template
import requests
import mysql.connector
from datetime import datetime
from datetime import date


data = {}
open = False
saveInfo = False

app = Flask(__name__)

#endpoint to communicate the rasberry with the web service
@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == 'POST'):
        tempJson = request.get_json()
        print(tempJson) 
        global open, data, saveInfo
        if (tempJson['20'] == '1'):
            open = True
            saveInfo = True
            while True:
                if (bool(data) != False ):
                    break
            temp = data
            data = {}
            saveInfo = False
            return jsonify(temp)
        elif (tempJson['20'] == '0'):
            open = False
            return ('',204)
    else:
        return jsonify({'Hola':'Pablo'})

#endpoint to communicate the the web page with web service
@app.route('/p', methods=['GET','POST'])
def page():
    if(request.method == 'POST'):
        global data 
        tempData = request.form.get("finfo")
        if(saveInfo == True):
            data['data']= tempData
        #return jsonify(data), 201
        return ('',204)
    else:
        if (open != False):
            return render_template("page.html"), 201
        else:
            return render_template("pagedown.html"), 201


if (__name__ == '__main__'):
    app.run(host='0.0.0.0',port=8080)