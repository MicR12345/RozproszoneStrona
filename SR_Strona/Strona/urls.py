from django.urls import path

from . import views

urlpatterns = [
    path('', views.DataList.as_view(), name=views.DataList.name),
    path('<int:pk>', views.DataDetail.as_view(), name=views.DataDetail.name),
    path('delete/<int:pk>', views.DataDelete.as_view(), name=views.DataDelete.name),
    path('add', views.DataAdd.as_view(), name=views.DataAdd.name),
    path('opis', views.Opis.as_view(), name=views.Opis.name),
]