import paho.mqtt.client as mqtt

#broker es el servidor MQTT a utilisar
#topic secuencia de palabras que identifican la publicacion
def mqttPublicador(broker, port, topic, data):
    client = mqtt.Client()
    client.connect(broker, port)

    try:
        result = client.publish(topic, str(data))
        print(f"Publicado: {str(data)} en {topic} -res {str(result)}")
    except KeyboardInterrupt:
        print("Publicación interrumpida.")
    finally:
        client.disconnect()

