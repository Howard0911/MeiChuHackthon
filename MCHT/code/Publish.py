import json
import time
import paho.mqtt.client as mqtt
import Constants as cst

def Publish(seq, mqttClient = mqtt.Client()):
    mqttClient.username_pw_set(username=cst.DEV_API_KEY,password=cst.DEV_API_KEY)
    mqttClient.connect(cst.MQTT_HOST, cst.MQTT_PORT, 60)
    data=[{"id":"position","value":[seq]}]
    mqttClient.publish(cst.PUB_PATH, json.dumps(data), 1)
    time.sleep(0.2)

def main():
    Publish("100111")

if __name__ == '__main__':
    main()