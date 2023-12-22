from rest_framework import serializers
from .models import UserAccount

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserAccount
        fields= '__all__'

class CustomUserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserAccount
        fields= ('id','username',)

class ObtainTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()