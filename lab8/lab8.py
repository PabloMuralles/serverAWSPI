from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == 'POST'):
        tempJson = request.get_json()
        print(tempJson) 
        if (tempJson['20'] == '1'):
            num = '1111001'
            return jsonify({'num':('{}'.format(num))}), 201
        else:
            return jsonify({'Respuesta':'No hacer nada'})
    else:
        return jsonify({'about':'Hola Pablo'})



if (__name__ == '__main__'):
    app.run(host='0.0.0.0',port=8080)