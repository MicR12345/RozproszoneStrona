from rest_framework import serializers

from .models import *

class DataSerializer(serializers.ModelSerializer):
    money = serializers.IntegerField()
    upgrade1 = serializers.IntegerField()

    class Meta:
        model = Data
        fields = ['money','upgrade1']