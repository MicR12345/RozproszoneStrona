from rest_framework import serializers

from .models import *

class DataSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    url = serializers.URLField()

    class Meta:
        model = Data
        fields = ['name','url']