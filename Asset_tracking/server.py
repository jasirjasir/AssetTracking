from flask import Flask, render_template, request
from flask import request
import os
import json
import math
from decimal import Decimal

app = Flask(__name__)
PEOPLE_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


beacondataSet = []
gateWayDataSet = []
localizationDataSet=[]
locationDataSet=[]

gatewayJson="E:/Python_Projects/Asset_tracking/gatewaylist.json"
textFile="E:/Python_Projects/Asset_tracking/tracking.txt"

PATH_LOSS_PARAMETER=3.0
isFirstHit=True

class Beacon:
    minorId = 0
    rssi = 0
    tx_power=0
    bleName = ""
    gatewayMac=""
    timestamp = ""
    

class GateWay:
    timestamp = ""
    macAddress = 0

class Localization:
    minorId=0
    x=0
    y=0
    rssi=0
    distance=0

class LocationData:
    gateway_name=""
    gateway_mac=""
    x=0
    y=0

@app.route("/")
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'warehouse.png')
    return render_template('index.html', user_image=full_filename)


@app.route("/test")
def hello():
    return "test!"


def writeToFile():
    try:

        f = open(textFile, "w")
        fileData=""
       # for item in gateWayDataSet:
            #fileData=fileData+"Time Stamp : "+item.timestamp+" - Mac Address: "+str (item.macAddress)+"\n"
        for item in beacondataSet:
            fileData=fileData+"BLE Name: "+item.bleName+" - Minor ID: "+str (item.minorId)+ " - Rssi: " +str(item.rssi)+ " - Gateway: "+item.gatewayMac+"\n"
           
        f.write(fileData)
        #print(fileData)
        f.close()
    except  e:
        print (e)
    pass


@app.route("/json-request", methods=['POST'])  # GET requests will be blocked
def json_request():
    req_data = request.get_json()
    global beacondataSet
    global gateWayDataSet
    global isFirstHit
    gatewayMac=""
    for item in req_data:
        if item["type"] == "Gateway":
            gateway = GateWay()
            gateway.macAddress = item["mac"]
            gateway.timestamp = item["timestamp"]
            gateWayDataSet.append(gateway)
            gatewayMac= item["mac"]
           
        if item.__contains__("ibeaconMinor") & item.__contains__("rssi") & item.__contains__("bleName"):
            beacondata = Beacon()
            beacondata.minorId = item["ibeaconMinor"]
            beacondata.rssi = item["rssi"]
            beacondata.bleName = item["bleName"]
            beacondata.timestamp = item["timestamp"]
            beacondata.tx_power=item["ibeaconTxPower"]
            beacondata.gatewayMac=gatewayMac
            beacondataSet.append(beacondata)
            performLocalization(beacondata)
    
    isFirstHit=False
    writeToFile()
    return "Success"
    

def performLocalization(beacondata) :
   
    global isFirstHit
    if(isFirstHit):
        obj_localize = Localization()
        obj_localize.minorId=beacondata.minorId
        obj_localize.rssi=beacondata.rssi
        obj_localize.distance=calculateDistance(beacondata.rssi,beacondata.tx_power)
        obj_localize.x=getvaluefromList(beacondata.gatewayMac,"x")
        obj_localize.y=getvaluefromList(beacondata.gatewayMac,"y")
        localizationDataSet.append(obj_localize)
    
    for  item in beacondataSet :
        if ((item.minorId==beacondata.minorId) and item.gatewayMac!=beacondata.gatewayMac and item.timestamp==beacondata.timestamp) :
                #print ("new element found ")
                obj_localize = Localization()
                obj_localize.minorId=beacondata.minorId
                obj_localize.rssi=beacondata.rssi
                obj_localize.distance=calculateDistance(beacondata.rssi,beacondata.tx_power)
                obj_localize.x=getvaluefromList(beacondata.gatewayMac,"x")
                obj_localize.y=getvaluefromList(beacondata.gatewayMac,"y")
                localizationDataSet.append(obj_localize)
                sortList(localizationDataSet)
                break
            
def getvaluefromList(mac,val):
    for item in locationDataSet:
        if (item.gateway_mac== mac) :
            if (val=='x'):
              return item.x
            elif (val=='y'):
              return item.y
              
def loadGatewayJson():
    file = open(gatewayJson,"r")
    data = json.load(file)
    for item in data['location_data']: 
        loc_data=LocationData()
        loc_data.gateway_name= item["gateway_name"]
        loc_data.gateway_mac= item["mac_id"]
        loc_data.x= int(item["x"])
        loc_data.y= int(item["y"])
        locationDataSet.append(loc_data)

def sortList (DataSet):
    posarray=[]
    distarray=[]
    filterList=[]

    for i in DataSet:
        posarray.append([i.x,i.y])
        distarray.append(i.distance)
        id=i.minorId
        for j in DataSet:
            if (j.minorId==id and j.x!=i.x and j.y!=i.y and (not(id in filterList))):
                posarray.append([j.x,j.y])
                distarray.append(j.distance)
        if(len(distarray)>=3):
            print ("Ready for trilateartion")
            print (posarray)
            print (distarray)

            x_out,y_out=applyTrilateration(posarray,distarray)
            print (x_out,y_out)
            print ("-------")
            posarray.clear()
            distarray.clear()
            filterList.append(id)
        else:
            print ("clearing array")
            posarray.clear()
            distarray.clear()
       
def applyTrilateration(posarray,distarray):
        
        # https://www.101computing.net/cell-phone-trilateration-algorithm/
        x1,y1,r1 =posarray[0][0],posarray[0][1],distarray[0]
        x2,y2,r2 =posarray[1][0],posarray[1][1],distarray[1]
        x3,y3,r3 = posarray[2][0],posarray[2][1],distarray[2]

        A = 2*x2 - 2*x1
        B = 2*y2 - 2*y1
        C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
        D = 2*x3 - 2*x2
        E = 2*y3 - 2*y2
        F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2
        x = (C*E - F*B) / (E*A - B*D)
        y = (C*D - A*F) / (B*D - A*E)
        return x,y



def calculateDistance(rssi,tx_power):
    ''' 
      RSSI = TxPower - 10 * n * lg(d) 
      n = 2 (in free space) 
      d = 10 ^ ((TxPower - RSSI) / (10 * n)) 

    ''' 
    dist= math.pow(10,  (tx_power - rssi) / (10 *PATH_LOSS_PARAMETER))
    return round(dist,3)

if __name__ == "__main__":
    loadGatewayJson()
    app.run()
