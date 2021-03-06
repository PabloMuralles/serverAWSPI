from flask import Flask, redirect, url_for, jsonify, request, render_template
import requests


data = {}
#open = False
saveInfo = False
numPage = 0
numBinaryPage = 0

app = Flask(__name__)

#endpoint to communicate the rasberry with the web service
@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == 'POST'):
        tempJson = request.get_json()
        print(tempJson) 
        numBinary = tempJson['num']
        numDecimal = int(numBinary,2)
        print(numDecimal)
        global data, saveInfo,numBinaryPage
        numBinaryPage = tempJson['num']
        saveInfo = True
        while True:
            if (bool(data) != False ):
                break
        temp = data
        data = {}
        saveInfo = False
        finalNum = numDecimal - numPage
        if (finalNum > 9):
            finalNum = finalNum - 10
            print(finalNum)
            finalNumBinary = ConvertNumToDisplay(finalNum) + '1'
            return jsonify({'num': str(finalNumBinary)}), 201
        else:
            finalNumBinary = ConvertNumToDisplay(finalNum) + '0'
            return jsonify({'num': str(finalNumBinary)}), 201
    else:
        return jsonify({'Hola':'Pablo'})

#endpoint to communicate the the web page with web service
@app.route('/p', methods=['GET','POST'])
def page():
    if(request.method == 'POST'):
        global data,numPage
        tempData = request.form.get("finfo")
        if(saveInfo == True):
            data['data']= tempData
            numPage = int(tempData)
        return ('',204)
    else:
        return render_template("page.html", data = numBinaryPage), 201

# 0 - 1111110#
# 1 - 0110000#
# 2 - 1101101#
# 3 - 1111001#
# 4 - 0110011#
# 5 - 1011011#
# 6 - 1011111#
# 7 - 1110000#
# 8 - 1111111#
# 9 - 1110011#
def ConvertNumToDisplay(data):
    if(data == 0):
        return '1111110' 
    elif(data == 1):
        return '0110000' 
    elif(data == 2):
        return '1101101' 
    elif(data == 3):
        return '1111001' 
    elif(data == 4):
        return '0110011' 
    elif(data == 5):
        return '1011011' 
    elif(data == 6):
        return '1011111' 
    elif(data == 7):
        return '1110000' 
    elif(data == 8):
        return '1111111'
    elif(data == 9):
        return '1110011'
     
     
    
if (__name__ == '__main__'):
    app.run(host='0.0.0.0',port=8080)