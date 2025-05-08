'''
Authors: Kalon Moco, Lexi Sario
Date: 5/7/23
Purpose: get data fom url, make table, analysis data

'''


import requests 
import json

r = requests.get('https://opensky-network.org/api/flights/all?begin=1746644400&end=1746648000')
s = requests.get('https://opensky-network.org/api/states/all')

data = s.json()

""" print(r.text) """
count1 = 0
for obj in r:
    count1 += 1
""" print("all flights in given time frame:", count1)
 """
count2 = 0
for obj in s:
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




'''
NOTES:

start times: 1746679440, 1746644400

end times: 1746683040, 1746648000

{"icao24":"c078fd","firstSeen":1517227317,"estDepartureAirport":"CYYZ","lastSeen":1517230676,"estArrivalAirport":"CYUL","callsign":"SWG9426 ","estDepartureAirportHorizDistance":525,"estDepartureAirportVertDistance":104,"estArrivalAirportHorizDistance":3244,"estArrivalAirportVertDistance":81,"departureAirportCandidatesCount":1,"arrivalAirportCandidatesCount":1}


["a35a97","N315NG  ","United States",1746682133,1746682133,-111.7467,35.216,6096,false,150.09,196.32,-0.65,null,6301.74,null,false,0]



'''