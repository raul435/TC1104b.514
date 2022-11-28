#include <ESP8266WiFi.h>


import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import time
from datetime import datetime
import random
# Application Default credentials are automatically created.
cred = credentials.Certificate('credentials.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

while True:
    print("Sending data")
    current_date = datetime.now()
    date = current_date.strftime('%Y-%m-%d')
    hour = current_date.strftime('%H')
    collectionName = u'database{0}'.format(date)
    encendido = bool(random.getrandbits(1))
    temperatura = int(random.uniform(0, 100))
    network_ref = db.collection(collectionName).document('network')
    network_doc = network_ref.get()
    network_data = network_doc.to_dict()
    network_ref.set({
        u'name': 'network',
        u'description': 'sensores de temperatura',
        u'region': 'guadalajara',
        u'numbsensors': 3,
    })
    for number in range(1, network_data['numbsensors']+1):
        subCollectionName = u'has'
        sensor_ref = db.collection(collectionName).document('network').collection(subCollectionName).document('sensor{0}'.format(number))
        sensor_doc = sensor_ref.get()
        sensor_data = sensor_doc.to_dict()
        sensor_ref.set({
            u'id': int(number),
            u'location': {
                u'latitude': 20.6767,
                u'longitude': -103.3496,
            },
            u'characteristics': {
            },
        })
        subSubCollectionName = u'records'
        temperature_ref = db.collection(collectionName).document('network').collection(subCollectionName).document('sensor{0}'.format(number)).collection(subSubCollectionName).document('temperature_h:{0}'.format(hour))
        temperature_doc = temperature_ref.get()
        temperature_data = temperature_doc.to_dict()
        if temperature_data == None:
            temperature_ref.set({
                u'timestamp': current_date,
                u'value': int(temperatura),
            })
        else:
            temperature_ref.update({
                u'timestamp': current_date,
                u'value': (int(temperature_data[u'value']) + temperatura)/2,
            })
        
        temperature_ref = db.collection(collectionName).document('network').collection(subCollectionName).document('sensor{0}'.format(number)).collection(subSubCollectionName).document('temperature_h:{0}'.format(date))
        temperature_doc = temperature_ref.get()
        temperature_data = temperature_doc.to_dict()
        if temperature_data == None:
            temperature_ref.set({
                u'timestamp': current_date,
                u'centigrados': int(temperatura),
                u'farenheit': (int(temperatura)*1.8)+32,
            })
        else:
            temperature_ref.update({
                u'timestamp': current_date,
                u'centigrados': int(temperature_data[u'centigrados']) + (int(temperatura))/2,
                u'farenheit': int(temperature_data[u'farenheit']) + ((int(temperatura)*1.8)+32)/2,
            })
        
    time.sleep(5)