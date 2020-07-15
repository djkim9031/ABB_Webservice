# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:35:45 2019

@author: KRDOKIM13
"""

#import sys
#import RestAPITesting as prog
from flask import Flask, render_template, request
import RobStart as RStart
import RobStop as RStop
import RestAPITestingSignals as RSignals
import sys

#prog.main(sys.argv[1:])



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/start")
def start():
    RStart.main(sys)
    return render_template("start.html")

@app.route("/stop")
def stop():
    RStop.main(sys)
    return render_template("stop.html")

@app.route("/signals")
def signals():
    json_value = RSignals.main(sys)
    name=[]
    value=[]
    for i in range(len(json_value)):
        name.append(json_value[i]['name'])
        value.append(json_value[i]['lvalue']) 
    
    return render_template("signals.html",name=name,value=value,length=len(name))

#@app.route("/jogging")
#def jogging():
#    return render_template("jogging.html")


@app.route('/handle_data', methods=['POST'])
def handle_data():
    signalName = request.form["signals"]
    json_value = RSignals.main(sys)
    for i in range(len(json_value)):
        if(json_value[i]['name']==signalName):
            value=json_value[i]['lvalue']
    return render_template("requestedSignal.html",signalName=signalName,value=value)

@app.route('/postmethod', methods = ['POST'])
def postmethod():
    jsdata = request.form.get('id')
    print(jsdata)
    return jsdata
      
if __name__ == "__main__":
    app.run(host='0.0.0.0')