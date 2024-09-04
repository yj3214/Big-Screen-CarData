from django.http import JsonResponse
from django.shortcuts import render
from .utils import getPublicData
from .utils import getCenterData
from .utils import getCenterLeftData
from .utils import getBottomLeftData
from .utils import getCenterRightData
from .utils import getCenterChangeData
from .utils import getBottomRightData
# Create your views here.

def center(request):
    if request.method == 'GET':
        sumCar, topCar, highVolume,  mostModel, mostBrand, average_price = getCenterData.getBaseData()
        lastSortList = getCenterData.getRollData()
        oilRate, electricRate, mixRate = getCenterData.getTypeRate()

        return JsonResponse({
            'sumCar': sumCar,
            'topCar': topCar,
            'highVolume': highVolume,
            'mostModel': mostModel,
            'mostBrand': mostBrand,
            'average_price': average_price,
            'lastSortList': lastSortList,
            'oilRate': oilRate,
            'electricRate': electricRate,
            'mixRate': mixRate
        })

def centerLeft(request):
    if request.method == 'GET':
        lastPieList = getCenterLeftData.getPieBrandData()
        return JsonResponse({
            'lastPieList': lastPieList
        })


def bottomLeft(request):
    if request.method == 'GET':
        brandList, volumeList, priceList = getBottomLeftData.getSquareData()
        return JsonResponse({
            'brandList': brandList,
            'volumeList': volumeList,
            'priceList': priceList,
        })

def centerRight(request):
    if request.method == 'GET':
        realData = getCenterRightData.getPriceSortData()
        return JsonResponse({
            'realData': realData
        })


def centerRightChange(request, energyType):
    if request.method == 'GET':
        oilData, electricData = getCenterChangeData.getCircleData()
        realData = []
        if energyType == 1: realData.extend(oilData)
        else: realData.extend(electricData)
        return JsonResponse({
            'realData': realData,
        })

def bottomRight(request):
    if request.method == 'GET':
        carData = getBottomRightData.getRankData()
        return JsonResponse({
            'carData': carData
        })