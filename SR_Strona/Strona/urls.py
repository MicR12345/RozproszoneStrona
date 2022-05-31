from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data', views.DataList.as_view(), name=views.DataList.name),
    path('data/<int:pk>', views.DataDetail.as_view(), name=views.DataDetail.name),
]