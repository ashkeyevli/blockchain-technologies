from django.shortcuts import render
import requests


# Create your views here.
API_KEY = 'c2d9966a-0e29-4251-82ac-59b98a2c8598'
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': API_KEY}


def index(request):
    context = {}
    return render(request, 'index.html', context)

def get_usd(request):
    try:
        amount = float(request.GET['amount'])
        response =  requests.get(URL, headers = headers)
        response_json = response.json()
        result = round(amount*response_json['data'][1]['quote']['USD']['price'],3)
        mydictionary = {
            "amount": amount,
            "answer": result,
            "error" : False,
            "result" : True
        }
        return render(request, "index.html", context = mydictionary)
    except:
        mydictionary = {
            "error" : True,
            "result" : False
        }
        return render(request, 'index.html', context=mydictionary)

