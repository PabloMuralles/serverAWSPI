from flask import Flask, redirect, url_for, jsonify, request, render_template
import requests


data = {}
numPage = 0

app = Flask(__name__)

#endpoint to communicate the rasberry with the web service
@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == 'POST'):
        tempJson = request.get_json()
        #print(tempJson)
        global data
        if (bool(data) == False ):
            return jsonify({'data':'null'})
        else:
            tempInsersion = data
            data = {}
            return jsonify(tempInsersion)
             
    else:
        return jsonify({'Hola':'Pablo'})

#endpoint to communicate the the web page with web service
@app.route('/p', methods=['GET','POST']) 
def page():
    if(request.method == 'POST'):
        global data,numPage
        tempData = request.form.get("finfo")
        if(len(tempData) <= 10 and len(tempData) > 0):
            if (tempData.isdecimal()):  
                data['data']= tempData
                numPage = int(tempData)
                return render_template("page.html", data = numPage), 201
            else:
                tempData2 = tempData
                tempData = ""
                for i in tempData2:
                    if i.isdecimal():
                        tempData+=i
                numPage = int(tempData)
                data['data']= tempData
                return render_template("page.html", data = tempData2), 201
        else:
            return render_template("page.html", data = 'numero mayor a 10 caracteres o no ingreso nada'), 201
    else:
        return render_template("page.html", data = numPage), 201 
    
if (__name__ == '__main__'):
    app.run(host='0.0.0.0',port=8080)