import json
import requests

from django.shortcuts import render
from django.views     import View
from django.http      import JsonResponse


class AirportInfoView(View):
   def get(self, request):
        url = 'https://gist.githubusercontent.com/creduo/90aafdc0d28a7b45ca6e75d82600a5cf/raw/69a67722ed3f82403751597fba5ca5cb4b576abd/airports.json'
        data = requests.get(url).json()
        k = request.GET.get("icao")
        result = data.values()
        for key in data.keys():
            if key == k:
                result["icao"]=k
             
        iata = request.GET.get("iata")
        r    = data.items()
        icao = r.keys()
        for v in data.keys():
            if icao == v:
               result["iata"]=iata 
        

        airport_info = {
                "icao" : result.icao,
                "iata" : result.iata,
                "name"  : result.name,
                "city"  : result.city,
                "state" : result.state,
                "country" : result.country,
                "elevation": result.elevation,
                "lat"    : result.latitude,
                "lon"    : result.longitude,
                "tz"     : result.tz,
            }
        return JsonResponse(airport_info, status=200)