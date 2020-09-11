from django.urls import path
from main.views import index, get_usd

urlpatterns = [
 path('', index),
 path('answear', get_usd, name='get_usd')
 ]