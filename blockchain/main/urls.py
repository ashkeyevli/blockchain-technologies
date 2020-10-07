from django.urls import path
from main.views import index, get_usd

urlpatterns = [
 path('', index),#url path=s to main html
 path('answear', get_usd, name='get_usd')#url path to answear pagw=
 ]