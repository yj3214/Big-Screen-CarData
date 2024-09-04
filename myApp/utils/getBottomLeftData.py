import json
import time
from .getPublicData import *

def getSquareData():
    cars = list(getAllCars())
    saleVolume = {}
    for i in cars:
        if saleVolume.get(str(i.carName), -1) == -1:
            saleVolume[str(i.carName)] = (int(i.saleVolume), json.loads(i.price)[0])
        else:
            saleVolume[str(i.carName)][0] += int(i.saleVolume)

    carVolume = sorted(saleVolume.items(), key=lambda x : x[1][0], reverse=True)[:14]

    brandList = []
    volumeList = []
    priceList = []
    for i in carVolume:
        brandList.append(i[0])
        volumeList.append(i[1][0])
        priceList.append(i[1][1])
    return brandList, volumeList, priceList