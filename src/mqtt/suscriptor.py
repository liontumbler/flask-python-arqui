import paho.mqtt.client as mqtt

# Función callback cuando se recibe un mensaje
def on_message(client, userdata, message):
    data = message.payload.decode("utf-8")
    print(f"Temperatura recibida: {data} en {client} -res {userdata}")

#broker es el servidor MQTT a utilisar
#topic secuencia de palabras que identifican la publicacion
def mqttSuscriptor(broker, port, topic, callback):

    client = mqtt.Client()

    # Asignar la función callback
    #client.on_message = on_message
    client.on_message = callback

    client.connect(broker, port)
    client.subscribe(topic)

    print("Esperando mensajes...")
    client.loop_forever()