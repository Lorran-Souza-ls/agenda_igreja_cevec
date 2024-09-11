import paho.mqtt.client as mqtt
from config.config import MQTT_BROKER, MQTT_PORT

def connect_mqtt():
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT)
    return client
