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

    def validate_fayl(self, value):
        if not value.endswith('.mp3'):
            raise serializers.ValidationError("Fayl faqat .mp3 formatida bo‘lishi kerak!")
        return value
