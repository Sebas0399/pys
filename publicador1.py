from paho.mqqt import client as cliente_mqtt
import time
import random
broker='10.0.2.15'
puerto=1884
tema="tema/test"
i=0
cliente=cliente_mqtt.Client()
def conectado(cliente,datos,flags,rc):
    if rc==0:
        print("Envio de lecturas")
    else:
        print("fallo la conexion",rc)
cliente.on_connect=conectado
cliente.connect(broker,puerto)
cliente.loop_start()
while i==0:
    datos=random.randint(0,100)
    cliente.publish(tema,datos)
    time.sleep(2)
cliente.disconnect()

