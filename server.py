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

from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print("hola desde el get")
        if "/sensor_1temp" in self.path:
            sensor_1_temp = self.path.split("=")[1]
            print("La temperatura es {}".format(sensor_1_temp))
            current_date = datetime.now()
            date = current_date.strftime('%Y-%m-%d')
            collectionName = u'sensor_1_{0}'.format(date)
            temp_ref = db.collection(collectionName).document('temperatura')
            temp_doc = temp_ref.get()
            temp_data = temp_doc.to_dict()
            if temp_data == None:
                temp_ref.set({
                    u'temperatura_promedio': sensor_1_temp
                })
            else:
                temp_ref.update({
                    u'temperatura_promedio': (int(temp_data[u'temperatura_promedio']) + int(sensor_1_temp))/2,
                })

        self._set_response()
        self.wfile.write("hola este es mi super server. GET request for {}".format(self.path).encode('utf-8'))



port=8080
server_address = ('', port)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()