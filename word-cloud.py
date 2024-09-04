import jieba
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import matplotlib.pyplot as ptl
from wordcloud import WordCloud
from pymysql import *
import json

def get_img(field, targetImageSrc, resImageSrc):
    con = connect(host='localhost',user='root',password='yj3214',database='cardata',port=3306, charset='utf8mb4')
    cursor = con.cursor()
    sql = f"select {field} from carinfo"
    cursor.execute(sql)
    data = cursor.fetchall()

    text = ''
    for i in data:
        if i[0] != '':
            tagArr = i
            for j in tagArr:
                text += j

    cursor.close()
    con.close()

    data_cur = jieba.cut(text, cut_all=False)
    string = ' '.join(data_cur)

    # 图片
    img = Image.open(targetImageSrc)
    img_arr = np.array(img)
    wd = WordCloud(
        font_path='STHUPO.TTF',
        mask=img_arr,
        background_color='#04122c'

    )
    wd.generate_from_text(string)
    # 绘制图片
    fig = ptl.figure(1)
    plt.imshow(wd)
    plt.axis('off')
    plt.savefig(resImageSrc, dpi=800, bbox_inches='tight',pad_inches=0)


get_img('muanfactuer', './big-screen-vue-datav/public/car.jpg','./big-screen-vue-datav/public/cloud-word.jpg')



