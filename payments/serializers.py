from rest_framework import serializers
from .models import Gateway, Payment


class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model= Gateway
        fiels=('id','title','descriptions','avatar')

# class PaymentSerializer (serializers.ModelSerializer):
#     class Meta: 
#         model= Payment
#         fiels= ('id','user','package','package','phone_number', 'created_time','update_time')       