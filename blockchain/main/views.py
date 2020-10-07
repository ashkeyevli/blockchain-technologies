from django.shortcuts import render
import requests


# Create your views here.
API_KEY = 'c2d9966a-0e29-4251-82ac-59b98a2c8598'#API key for website coinmarket
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'#url to access latest cryptocurrency prices and information
headers = {'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': API_KEY}#header with API key for coinmarket website


def index(request):# function for representing start page index.html
    context = {}
    return render(request, 'index.html', context)#The template is executed with the passed word of text and returns an HttpResponse with the content received.

def get_usd(request):#function for converting etherium to usd
    try:
        amount = float(request.GET['amount'])#getting amount of etherium from input in index.html
        response =  requests.get(URL, headers = headers)#getting response from coinmarketcap website with all cryptocurrency information
        response_json = response.json()#getting json of response
        result = round(amount*response_json['data'][1]['quote']['USD']['price'],3)# selecting from json etherium price for USD, multipling it to the entered amount and round it to 3 digits.
        mydictionary = {
            "amount": amount,#setting for dictionary amount entered
            "answer": result,#setting result with converted etherium to USD
            "error" : False,#setting no error
            "result" : True#setting result boolean true
        }
        return render(request, "index.html", context = mydictionary)#returns HttpResponse with the content
    except:
        mydictionary = {
            "error" : True,#if was error set bool error true
            "result" : False#no result
        }
        return render(request, 'index.html', context=mydictionary)#returns HttpResponse with setted dictionary

