#include <ESP8266WiFi.h>

// Credenciales wifi
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

#define ssid
#define password
// server to connect to and relative path to PHP script
char server[] = "8080-raul435-tc1104b514-0pdpn1rv7ln.ws-us77.gitpod.io";
String url = "/sensor_1temp=";

bool iterar = true;

void setup()
{
Serial.begin(115200);
Serial.println();

WiFi.begin(ssid, password);

while (WiFi.status() != WL_CONNECTED)
{
Serial.print(".");
delay(250);
}
Serial.print("\nConectado al Wi-Fi");
Serial.println();
Serial.println("Connecting to server...");
Serial.println(server);
WiFiClientSecure client;
client.setInsecure();
const int httpPort = 443;
if (!client.connect(server, httpPort)) {
Serial.println("connection failed");
return;
}

Serial.print("Requesting URL: ");
Serial.println(url);

client.print(String("GET ") + url + "40" + " HTTP/1.1\r\n" +
"Host: " + server + "\r\n" +
"Connection: close\r\n\r\n");

// Close connecting
Serial.println();
Serial.println("closing connection");
}

void loop(){
    
} // End Loop