from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Settlement, Carrier

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password' : {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class SettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settlement
        fields = ('id', 'title','settlement_type', 'start_date', 'end_date', 'year', 'quarter', 'stop_count', 'route_count', 'revenue', 'check_number', 'paid', 'carrier')

class CarrierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carrier
        fields = ('company_name', 'user')