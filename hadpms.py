import paho.mqtt.client as mqtt
import subprocess

# MQTT Settings
mqtt_broker = "homeassistant server ip"
mqtt_port = 1883
mqtt_topic = "/homeassistant/sensor/dpms/lcd"
mqtt_username = "user"
mqtt_password = "password"

# Define callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code "+str(rc))
    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print(f"Received message on topic {msg.topic}: {payload}")

    if payload == "ON":
        subprocess.call(["xset", "dpms", "force", "on"])
        subprocess.call(["xset", "s", "noblank"])
        subprocess.call(["xset", "s", "off"])
        subprocess.call(["xset", "-dpms"])
    elif payload == "OFF":
        subprocess.call(["xset", "dpms", "force", "off"])

# Create MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Set MQTT username and password
client.username_pw_set(mqtt_username, mqtt_password)

# Connect to MQTT Broker
client.connect(mqtt_broker, mqtt_port, 60)

# Start the MQTT loop
client.loop_forever()


