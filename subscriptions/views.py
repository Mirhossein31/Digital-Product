from django.utils import timezone
from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated ,IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Subscription , Package
from .serializers import PackageSerializer, SubscriptionSerializer


class PackageView (APIView):
     def get(self,request):
        packages=Package.objects.filters(is_enable=True)
        serializer= PackageSerializer(packages, many=True)
        return Response(serializer.data)

class SubscriptionView(APIView) :
    permission_classes= [IsAuthenticated]   

    def get(self, request) :
        subscriptions=Subscription.objects.filter(
            user= request.user,
            expired_time__gt=timezone.now()
        )
        serializer=SubscriptionSerializer (subscriptions, many=True)
        return Response(serializer.data)