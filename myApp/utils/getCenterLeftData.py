import json
import time
from .getPublicData import *

def getPieBrandData():
    cars = list(getAllCars())
    carsVolume = {}
    for i in cars:
        if carsVolume.get(str(i.brand), -1) == -1:
            carsVolume[str(i.brand)] = int(i.saleVolume)
        else:
            carsVolume[str(i.brand)] += int(i.saleVolume)
    carsVolume = sorted(zip(carsVolume.values(), carsVolume.keys()), reverse=True)
    lastPieList = [{"name": i[1], 'value': i[0]} for i in carsVolume][:10]
    # print(lastPieList)
    return lastPieList