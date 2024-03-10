#Aula 30 - Requisições HTTP em Python
#HMAP - 22/03/2020
#Aula 36 - Obtendo Clima Atual
#HMAP - 18/04/2020
#Módulo da requisição
import requests
#Dicionário da requisição
import json
#Módulo para imprimir o dicionário
import pprint

accuweatherAPIKey = 'INSERT YOUR KEY HERE'
r = requests.get('http://www.geoplugin.net/json.gp')
#Verificação de localização, baseado na numeração de erro 200
if (r.status_code != 200):
    print('Não foi possível obter a localização.')
else:
    #print(r.text) - dados da requisição http
    localizacao = json.loads(r.text)
    lat = localizacao['geoplugin_latitude']
    long = localizacao['geoplugin_longitude']
    "print('lat: ', lat)"
    "print('long: ', long)"
    
    LocationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=" + accuweatherAPIKey + "&q=" + lat + "%2C" + long + "&language=pt-br"
    
    r2 = requests.get(LocationAPIUrl)
    if (r2.status_code != 200):
        print('Não foi possível obter a localização.')
    else:
        locationResponse = json.loads(r2.text)
        nomeLocal = locationResponse['LocalizedName'] + "," + locationResponse['AdministrativeArea']['LocalizedName'] + "." + locationResponse['Country']['LocalizedName']
        codigoLocal = locationResponse['Key']
        print("Obtendo clima do local: ", nomeLocal)
        "print('Código do Local: ', codigoLocal)"
        
        CurrentConditionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" + codigoLocal + "?apikey=" + accuweatherAPIKey + "&language=pt-br"

        r3 = requests.get(CurrentConditionsAPIUrl)
        if (r3.status_code != 200):
            print('Não foi possível obter a localização.')
        else:
            CurrentConditionsResponse = json.loads(r3.text)
            "print(pprint.pprint(CurrentConditionsResponse))"
            textoClima = CurrentConditionsResponse[0]['WeatherText']
            temperatura = CurrentConditionsResponse[0]['Temperature']['Metric']['Value']
            print('Clima no momento: ', textoClima)
            print('Temperatura no momento: '+ str(temperatura) + ' graus Celsius')