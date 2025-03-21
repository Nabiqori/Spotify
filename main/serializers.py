from datetime import timedelta

from rest_framework import serializers
from .models import *

class QoshiqchiSerializer(serializers.ModelSerializer):

    class Meta:
        model=Qoshiqchi
        fields='__all__'

class AlbomSerializer(serializers.ModelSerializer):

    class Meta:
        model= Albom
        fields='__all__'

class JadvalSerializer(serializers.ModelSerializer):

    class Meta:
        model=Jadval
        fields='__all__'

    def     validate_fayl(self, value):
        if not value.name.endswith('.mp3'):
            raise serializers.ValidationError("Fayl faqat .mp3 formatida bo‘lishi kerak!")
        return value

    def validate_davomiylik(self, value):
        if value > timedelta(minutes=7):
            raise serializers.ValidationError("Qo‘shiq davomiyligi 7 daqiqadan oshmasligi kerak!")
        return value

