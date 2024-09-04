import requests
from lxml import etree
import csv
import os
import time
import json
import pandas as pd
import re
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CarBigScreen.settings')
django.setup()
from myApp.models import CarInfomation
class spider(object):
    def __init__(self):
        self.spiderUrl = "https://www.dongchedi.com/motor/pc/car/rank_data?aid=1839&app_name=auto_web_pc&city_name=%E5%8C%97%E4%BA%AC&count=10&month=&new_energy_type=&rank_data_type=11&brand_id=&price=&manufacturer=&outter_detail_type=&nation=0"
        self.headers = {
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
        }
    def init(self):
        if not os.path.exists('./temp.csv'):
            with open('./temp.csv', 'a', newline='', encoding='utf-8') as wf:
                write = csv.writer(wf)
                write.writerow(["brand","carName", "carImg", "saleVolume", "price", "muanfactuer", "rank", "carModel",
                                "energeType", "marketTime", "insure"])
    def get_page(self):
        with open('./spiderPage.txt', 'r') as rf:
            return rf.readlines()[-1].strip()

    def set_page(self, newPage):
        with open('./spiderPage.txt', 'a') as wf:
            wf.write('\n'+ str(newPage))

    def main(self):
        count = self.get_page()
        params = {
            "offset": int(count)
        }
        print("数据从{}开始爬取".format(int(count) + 1))
        pageJson = requests.get(self.spiderUrl, headers=self.headers, params=params).json()
        pageJson = pageJson["data"]["list"]
        for index, car in enumerate(pageJson):
            try:
                print("正在爬取第{}个数据".format(index+int(count)+1))
                # 品牌名， 车名， 图片链接， 销量
                carData = [car["brand_name"], car["series_name"], car["image"], car["count"]]
                # 最低价 和 最高价
                price = [car["min_price"], car["max_price"]]
                carData.append(price)
                # 厂商 销量排名
                carData.extend([car["sub_brand_name"], car["rank"]])
                # 进一步获取其他信息
                infoHTML = requests.get("https://www.dongchedi.com/auto/params-carIds-x-{}".format(car["series_id"]),
                                        headers=self.headers)
                infoHTMLpath = etree.HTML(infoHTML.text)
                # 车型
                carModel = infoHTMLpath.xpath("//div[@data-row-anchor='jb']/div[2]/div/text()")[0]
                # 能源类型
                energyType = infoHTMLpath.xpath("//div[@data-row-anchor='fuel_form']/div[2]/div/text()")[0]
                # 上市时间
                marketTime = infoHTMLpath.xpath("//div[@data-row-anchor='market_time']/div[2]/div/text()")[0]
                # 保修期限
                insure= infoHTMLpath.xpath("//div[@data-row-anchor='period']/div[2]/div/text()")[0]
                carData.extend([carModel, energyType, marketTime, insure])
                print(carData)
                self.save_to_csv(carData)
            except:
                pass
        self.set_page(int(count) + 10)
        self.main()
    def save_to_csv(self, resultData):
        with open('./temp.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(resultData)
    def clear_csv(self):
        df = pd.read_csv('./temp.csv')
        # 处理缺失值
        df.dropna(inplace=True)
        # 去除重复数据
        df.drop_duplicates(inplace=True)
        print("总数量为：{}".format(df.shape[0]))
        return df.values

    def save_to_sql(self):
        data = self.clear_csv()
        for car in data:
            CarInfomation.objects.create(
                brand=car[0],
                carName=car[1],
                carImg=car[2],
                saleVolume=car[3],
                price=car[4],
                muanfactuer=car[5],
                rank=car[6],
                carModel=car[7],
                energeType=car[8],
                marketTime=car[9],
                insure=car[10],
            )


if __name__ == '__main__':
    spiderObj = spider()
    # spiderObj.init()
    # spiderObj.main()
    spiderObj.save_to_sql()