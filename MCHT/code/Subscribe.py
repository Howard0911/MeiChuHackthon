import json
import time
import paho.mqtt.client as mqtt
import Constants as cst

mqttClient = mqtt.Client()

def on_mqtt_connect():
    mqttClient.username_pw_set(username=cst.DEV_API_KEY,password=cst.DEV_API_KEY)
    mqttClient.connect(cst.MQTT_HOST, cst.MQTT_PORT, 60)
    mqttClient.loop_start()
    # mqttClient.loop_forever()

def on_publish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)

def on_message_come(lient, userdata, msg):
    print(msg.topic + " " + ":" + str(msg.payload))

def on_subscribe():
    mqttClient.subscribe("/v1/device/19151157062/sensor/position/rawdata", 1)
    mqttClient.on_message = on_message_come

def main():
    on_mqtt_connect()
    data=[{"id":"position","value":["0000101"]}]
    on_publish("/v1/device/19151157062/rawdata", json.dumps(data), 1)
    on_subscribe()
    while True:
        pass

if __name__ == '__main__':
    main()