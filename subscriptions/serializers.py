from rest_framework import serializers
from .models import Package, Subscription

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model= Package
        fields= ('id','title', 'sku','desciption', 'avatar', 'price', 'duration')

class SubscriptionSerializer(serializers.ModelSerializer):
    Package= PackageSerializer()
    class Meta:
        modle=Subscription
        fields= ('pakage', 'created_time','expire_time')    