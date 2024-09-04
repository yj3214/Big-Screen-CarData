import json
import time
from .getPublicData import *



def getCircleData():
    cars = list(getAllCars())
    oilData = []
    electricData = []

    for i in cars:
        if i.energeType == '汽油':
            oilData.append([i.carName, i.saleVolume, i.energeType])
        elif i.energeType == '纯电动':
            electricData.append([i.carName, i.saleVolume, i.energeType])

    oilData = oilData[:10]
    electricData = electricData[:10]
    return oilData, electricData