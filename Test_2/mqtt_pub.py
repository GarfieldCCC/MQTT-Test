import paho.mqtt.client as mqtt

HOST = "127.0.0.1"
PORT = 1883
mqttClient = mqtt.Client()


# 连接MQTT服务器
def on_mqtt_connect():
    mqttClient.connect(host=HOST, port=PORT, keepalive=600)
    mqttClient.loop_start()


# publish 消息
def on_publish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)


# 消息处理函数
def on_message_come(client, userdata, msg):
    print(msg.topic + " " + ":" + str(msg.payload))


# subscribe 消息
def on_subscribe():
    mqttClient.subscribe(topic="chat", qos=2)
    mqttClient.on_message = on_message_come  # 消息到来处理函数


def main():
    on_mqtt_connect()
    on_publish(topic="chat", payload="Hello Python!", qos=2)
    on_subscribe()
    while True:
        pass


if __name__ == '__main__':
    main()
