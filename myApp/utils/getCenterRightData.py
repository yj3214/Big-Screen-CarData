import json
import time
from .getPublicData import *


def getPriceSortData():
    cars = list(getAllCars())
    priceSortList = {
        '0-5w': 0,
        '5-10w': 0,
        '10-20w': 0,
        '20-30w': 0,
        '30w以上': 0,
    }
    for i in cars:
        price = json.loads(i.price)[0]
        if price < 5: priceSortList['0-5w'] += 1
        elif price >= 5 and price < 10: priceSortList['5-10w'] += 1
        elif price >= 10 and price < 20: priceSortList['10-20w'] += 1
        elif price >= 20 and price < 30: priceSortList['20-30w'] += 1
        else: priceSortList['30w以上'] += 1
    realData = [{'name': k, 'value': v} for k, v in priceSortList.items()]
    return realData