from flask import Flask, render_template, request
from hotel import Hotel
from loader import LoadHotelsData
from indexer import Indexer

hotelsEngines = {}
app = Flask(__name__)

def IndexHotel(_hotelName):
    hotelsEngines[_hotelName].Index()

def IndexAll():
    for hotelName in hotelsEngines.keys():
        hotelsEngines[hotelName].Index()

def InitApp():
    hotelsInfo = LoadHotelsData()
    indexer = Indexer()
    for i, name in enumerate(hotelsInfo.keys()):
        hotelsEngines[name] = Hotel(indexer, name, hotelsInfo[name], i)

@app.route('/')
def index():
    return render_template("index.html", hotels=list(hotelsEngines.keys()))

@app.route('/GetReviewsTones', methods=["POST"])
def GetReviewsTons():
    hotelName = request.form['name']
    hotelsNames = list(hotelsEngines.keys())
    if(hotelName not in hotelsNames):
        return "hotel name is not exist"
    reviews = hotelsEngines[hotelName].Analyze()
    return render_template("hotelRewiewsTable.html", reviews=reviews)

@app.route('/IndexData', methods=["POST"])
def IndexData():
    if "name" in request.form:
        IndexHotel(request.form["name"])
    else:
        IndexAll()

    return "done"

if __name__ == '__main__':
    InitApp()
    app.run(port = 8080, debug=True) 