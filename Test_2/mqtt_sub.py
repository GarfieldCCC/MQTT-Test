import paho.mqtt.client as mqtt

HOST = "127.0.0.1"
PORT = 1883


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("chat")


def on_message(client, userdata, msg):
    print(msg.topic + " " + ":" + str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host=HOST, port=PORT, keepalive=600)
client.loop_forever()
