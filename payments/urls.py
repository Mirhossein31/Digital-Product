from django.urls import path
from .views import Gatwayview ,PaymentView

urlpatterns = [
    path('gateways/', Gatwayview.as_view),
    path('payments/', PaymentView.as_view),
]