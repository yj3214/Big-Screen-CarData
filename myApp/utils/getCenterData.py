import json
import time
from .getPublicData import *
def getBaseData():
    cars = getAllCars()
    # 数据总量
    sumCar = len(cars)
    # 销售最多汽车
    topCar = cars[0].carName
    # 车辆最高销售额
    highVolume = cars[0].saleVolume
    # 销售最多车型
    carModels = {}
    maxModel = 0
    mostModel = ''
    for i in cars:
        if carModels.get(i.carModel, -1) == -1:
            carModels[str(i.carModel)] = 1
        else:
            carModels[str(i.carModel)] += 1
    carModels = sorted(carModels.items(), key=lambda x:x[1], reverse=True)
    mostModel = carModels[0][0]
    # 车型最多品牌
    carBrands = {}
    maxBrand = 0
    mostBrand = ''
    for i in cars:
        if carBrands.get(i.brand, -1) == -1:
            carBrands[str(i.brand)] = 1
        else:
            carBrands[str(i.brand)] += 1
    for k, v in carBrands.items():
        if v > maxBrand:
            maxBrand = v
            mostBrand = k
    # 车辆平均价格
    average_price = sum([sum(json.loads(i.price)) for i in cars])/(len(cars)*2)
    average_price = round(average_price, 2)

    return sumCar, topCar, highVolume,  mostModel, mostBrand, average_price

def getRollData():
    cars = list(getAllCars())
    # 品牌
    carBrands = {}
    for i in cars:
        if carBrands.get(i.brand, -1) == -1:
            carBrands[str(i.brand)] = 1
        else:
            carBrands[str(i.brand)] += 1
    brandList = [(k, v) for k, v in carBrands.items()]
    brandList = sorted(brandList, reverse=True, key=lambda x: x[1])[:10]
    brandDict = [{'name':i[0],'value': i[1]} for i in brandList]
    return brandDict

def getTypeRate():
    cars = list(getAllCars())
    # 能源类型
    carTypes = {}
    for i in cars:
        if carTypes.get(str(i.energeType), -1) == -1:
            carTypes[str(i.energeType)] = 1
        else:
            carTypes[str(i.energeType)] += 1
    # 油车比率
    oilRate = round(carTypes['汽油'] / len(cars) * 100, 2)
    # 电车比率
    electricRate = round(carTypes['纯电动'] / len(cars) * 100, 2)
    # 混合动力
    mixRate = round(100 - oilRate - electricRate, 2)
    return oilRate, electricRate, mixRate


