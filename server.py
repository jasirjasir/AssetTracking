from flask import Flask, render_template, request
from flask import request
import os
import json

PEOPLE_FOLDER = os.path.join('static', 'people_photo')
beacondataSet = []
gateWayDataSet = []

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


class Beacon:
    minorId = 0
    rssi = 0
    bleName = ""


class GateWay:
    timestamp = ""
    macAddress = 0


@app.route("/")
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'warehouse.png')
    return render_template('index.html', user_image=full_filename)


@app.route("/hello")
def hello():
    return "Hello World!"


def writeToFile():
    f = open("tracking.txt", "w")
    fileData=""
    for item in gateWayDataSet:
        fileData=fileData+"Time Stamp : "+item.timestamp+" - Mac Address: "+str (item.macAddress)+"\n"
    for item in beacondataSet:
        fileData=fileData+"BLE Name: "+item.bleName+" - Minor ID: "+str (item.minorId)+ " - Rssi: "+str(item.rssi)+"\n"
    f.write(fileData)
    f.close()
    pass


@app.route("/json-example", methods=['POST'])  # GET requests will be blocked
def json_example():
    req_data = request.get_json()
    global beacondataSet
    global gateWayDataSet
    for item in req_data:
        if item.has_key("ibeaconMinor") & item.has_key("rssi") & item.has_key("bleName"):
            data = Beacon()
            data.minorId = item["ibeaconMinor"]
            data.rssi = item["rssi"]
            data.bleName = item["bleName"]
            beacondataSet.append(data)
        if item["type"] == "Gateway":
            gateway = GateWay()
            gateway.macAddress = item["mac"]
            gateway.timestamp = item["timestamp"]
            gateWayDataSet.append(gateway)
    writeToFile()
    return "Received data from Gateway"
    # return "hello"


if __name__ == "__main__":
    app.run()
