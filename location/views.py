from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.


def homeView(request):
    return render(request, 'location/index.html')


@method_decorator(csrf_exempt, name='dispatch')
class testAPI(View):
    def get(self, request):
        requestData = json.loads(request.body)
        pointsList = []
        for keys in requestData:
            print(requestData[keys])
            REVERSEGEOCODE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'
            ENDPOINT = 'key=<APIKEY>&address='+requestData[keys]
            r = requests.get(REVERSEGEOCODE_URL+ENDPOINT)
            pointsList.append([r.json()['results'][0]['geometry']['location']['lat'], r.json()['results'][0]['geometry']['location']['lng']])

        DISTANCEURL = 'https://api.distancematrix.ai/maps/api/distancematrix/json?'
        ENDPOINT = 'key<APIKEY>&origins=' + str(pointsList[0][0])+','+str(pointsList[0][1])+'&destinations='+str(pointsList[1][0])+','+str(pointsList[1][1])
        r = requests.get(DISTANCEURL+ENDPOINT)
        data = r.json()
        print(data)
        return JsonResponse(data)
