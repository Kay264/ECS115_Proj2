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

api = requests.get('https://opensky-network.org/api/states/all')
flights = requests.get('https://opensky-network.org/api/flights/all?begin=1746644400&end=1746648000')

states = requests.get('https://opensky-network.org/api/states/all')
data = states.json()
states = data.get('states', []) 

''' # code to create json file with data, make sure to uncomment for submission?
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(states, f, ensure_ascii=False, indent=4)
'''

# Function to calculate average of a property of a flight
def avg_count(property): 
    sum = 0
    count = 0

    for state_vector in states:
        if isinstance(state_vector, list) and len(state_vector) > 13 and isinstance(state_vector[property], (int, float)):
            sum += state_vector[property]
            count += 1
    
    return (sum/count)

print("Connection check:", api) # checks if connection is successful (200 response)

# #1
print("\n1. Plot the number of planes in the air over time.")

# reference this i think and use matplotlib. make this look less like doodoo maybe if we can
a = requests.get('https://opensky-network.org/api/flights/all?begin=1746644400&end=1746648000')
'''
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
'''

numA = 0
for obj in a:
    numA += 1

'''
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

'''

print(a.text)
# numList = [numA, numB, numC, numD, numE, numF, numG, numH, numI, numJ, numK]

# print(numList)

# #2
print("\n2. How many planes are in the air right now?")
planes = 0
for obj in states: # count each object in states
    planes += 1
print(planes, "planes are in the air right now")

# #3
print("\n3. What is the average altitude and speed of active planes?")
print("Average Altitude:", avg_count(13), "meters")
print("Average Speed:", avg_count(9), "meters per second")

# #4
print("\n4. Where are the flights concentrated right now?")
print("Average Longitude:", avg_count(5), "degrees")
print("Average Latitude:", avg_count(6), "degrees")
