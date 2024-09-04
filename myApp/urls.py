from django.urls import path

from myApp import views
urlpatterns = [
    path('center/', views.center, name='center'),
    # 左上角饼图
    path('centerLeft/', views.centerLeft, name='centerLeft'),
    # 左下角柱状图
    path('bottomLeft/', views.bottomLeft, name='bottomLeft'),
    # 右上角胶囊柱图
    path('centerRight/', views.centerRight, name='centerRight'),
    # 轮播图
    path('centerRightChange/<int:energyType>', views.centerRightChange, name='centerRightChange'),
    # 排行榜
    path('bottomRight/', views.bottomRight, name='bottomRight'),
]