import json
import time
from .getPublicData import *


def getRankData():
    cars = list(getAllCars())
    carData = []
    for car in cars:
        car.price = json.loads(car.price)
        car.price = '-'.join([str(i) for i in car.price])
        carData.append({
            'carName': car.carName,
            'brand': car.brand,
            'rank': car.rank,
            'carImg':car.carImg,
            'manufacturer': car.muanfactuer,
            'carModel': car.carModel,
            'price': car.price,
            'saleVolume': car.saleVolume,
            'marketTime': car.marketTime,
            'insure': car.insure
        })
    return carData