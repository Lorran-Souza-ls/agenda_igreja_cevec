import time
from utils.iot_utils import connect_mqtt

def collect_data():
    client = connect_mqtt()
    client.subscribe("sensor/data")
    
    def on_message(client, userdata, message):
        data = message.payload.decode()
        print(f"Data received: {data}")
    
    client.on_message = on_message
    client.loop_start()
    
    time.sleep(10)  # Coleta dados por 10 segundos
    client.loop_stop()
