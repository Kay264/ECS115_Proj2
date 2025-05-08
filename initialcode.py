'''
Authors: Kalon Moco, Lexi Allyson Sario
Date: 5/7/23
ECS 115 - Computer Networks

Project 2 - API Interaction and Automation Tool for Open Sky Flight
Purposes:
    - fetch and automate data
    - stores data and displays it in a json file
    - plots data over time via matplotlib
'''

import requests 
import json

##### kalon code

api = requests.get('https://opensky-network.org/api/states/all')
flights = requests.get('https://opensky-network.org/api/flights/all?begin=1746644400&end=1746648000')
states = requests.get('https://opensky-network.org/api/states/all')

data = states.json()


print(api) 

count1 = 0
for obj in flights:
    count1 += 1
""" print("all flights in given time frame:", count1)
 """
count2 = 0
for obj in states:
    count2 += 1
""" print("all  flights now:", count2) """


states = data.get('states', []) 

sum = 0
count3 = 0

for state_vector in states:
    if isinstance(state_vector, list) and len(state_vector) > 13 and isinstance(state_vector[13], (int, float)):
         sum += state_vector[13]
         count3 += 1

""" print(sum)
print(count3)
print(sum/count3) """

sum2 = 0
count4 = 0

for state_vector in states:
    if isinstance(state_vector, list) and len(state_vector) > 13 and isinstance(state_vector[9], (int, float)):
         sum2 += state_vector[9]
         count4 += 1

""" print(sum2)
print(count4)
print(sum2/count4) """


sum3 = 0
count5 = 0

for state_vector in states:
    if isinstance(state_vector, list) and len(state_vector) > 13 and isinstance(state_vector[5], (int, float)):
         sum3 += state_vector[5]
         count5 += 1

""" print(sum3)
print(count5)
print("Average Longitude:", sum3/count5) """

sum4 = 0
count6 = 0

for state_vector in states:
    if isinstance(state_vector, list) and len(state_vector) > 13 and isinstance(state_vector[6], (int, float)):
         sum4 += state_vector[6]
         count6 += 1
""" 
print(sum4)
print(count6)
print("Average Latitude:", sum4/count6) """




""" 

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(states, f, ensure_ascii=False, indent=4)
 """


a = requests.get('https://opensky-network.org/api/flights/all?begin=1746644400&end=1746648000')
b = requests.get('https://opensky-network.org/api/flights/all?begin=1746648000&end=1746651600')
c = requests.get('https://opensky-network.org/api/flights/all?begin=1746651600&end=1746655200')
d = requests.get('https://opensky-network.org/api/flights/all?begin=1746655200&end=1746648000')
e = requests.get('https://opensky-network.org/api/flights/all?begin=1746648000&end=1746658800')
f = requests.get('https://opensky-network.org/api/flights/all?begin=1746658800&end=1746662400')
g = requests.get('https://opensky-network.org/api/flights/all?begin=1746662400&end=1746666000')
h = requests.get('https://opensky-network.org/api/flights/all?begin=1746666000&end=1746669600')
i = requests.get('https://opensky-network.org/api/flights/all?begin=1746669600&end=1746673200')
j = requests.get('https://opensky-network.org/api/flights/all?begin=1746673200&end=1746676800')
k = requests.get('https://opensky-network.org/api/flights/all?begin=1746676800&end=1746680400')

numA = 0
for obj in a:
    numA += 1

numB = 0
for obj in b:
    numB += 1

numC = 0
for obj in c:
    numC += 1

numD = 0
for obj in d:
    numD += 1

numE = 0
for obj in e:
    numE += 1

numF = 0
for obj in f:
    numF += 1

numG = 0
for obj in g:
    numG += 1

numH = 0
for obj in h:
    numH += 1

numI = 0
for obj in i:
    numI += 1

numJ = 0
for obj in j:
    numJ += 1

numK = 0
for obj in k:
    numK += 1

numList = [numA, numB, numC, numD, numE, numF, numG, numH, numI, numJ, numK]

print(numList)



'''
NOTES:

start times: 1746679440, 1746644400

end times: 1746683040, 1746648000

{"icao24":"c078fd","firstSeen":1517227317,"estDepartureAirport":"CYYZ","lastSeen":1517230676,"estArrivalAirport":"CYUL","callsign":"SWG9426 ","estDepartureAirportHorizDistance":525,"estDepartureAirportVertDistance":104,"estArrivalAirportHorizDistance":3244,"estArrivalAirportVertDistance":81,"departureAirportCandidatesCount":1,"arrivalAirportCandidatesCount":1}


["a35a97","N315NG  ","United States",1746682133,1746682133,-111.7467,35.216,6096,false,150.09,196.32,-0.65,null,6301.74,null,false,0]



'''