# Import libraries 
import paho.mqtt.client as mqtt

# Set callbacks
def on_message(client, userdata, message):
    # Get data about message:
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
       
    # Publish message to cloud
    print("Publishing message to cloud:")
    client_cloud.publish(topic, payload=messasge.payload)

# Local client
client_local = mqtt.Client("local") 
client_local.on_message=on_message 
client_local.connect("local ip") 
client_local.subscribe("topic")

# Cloud client
client_cloud = mqtt.Client("cloud") 
client_cloud.connect("cloud ip")
client_cloud.loop_forever()