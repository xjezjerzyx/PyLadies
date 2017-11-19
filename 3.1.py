import sys
import requests
#Korzystając z API https://swapi.co/api/. Wyświetl imiona wszytkich Gunganów w języku Wooki.
# resp = requests.get('https://swapi.co/api/')

param = {"name": "Millennium Falcon"}
paramPlan = ''
#resp = requests.get('https://swapi.co/api/people?search=c-3po')
resp = requests.get('https://swapi.co/api/starships?search=Millennium')
resp2 = requests.get('https://swapi.co/api/starships/', params=param)
print(resp2.url)

resp_txt = resp2.content

resp_json = resp.json()
print(resp2.status_code)

#for a in resp_json:
#    if resp_json[a]['name'] == "Luke Skywalker":
#        print('yyy')


#print(resp_txt["name"])