from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('Strona.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]