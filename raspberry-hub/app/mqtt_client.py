import json
import time

import paho.mqtt.client as mqtt

from logger import log


class MQTTClient:
    def __init__(self, config: dict):
        self.node_id = config["nodeId"]

        self.host = config["mqtt"]["host"]
        self.port = config["mqtt"]["port"]

        self.availability_topic = (
            f"rhh/{self.node_id}/availability"
        )

        self.heartbeat_topic = (
            f"rhh/{self.node_id}/heartbeat"
        )

        self.command_topic = "rhh/hub/commands"

        self.client = mqtt.Client(
            client_id=self.node_id,
            clean_session=True
        )

        offline_payload = {
            "nodeId": self.node_id,
            "status": "offline",
            "timestamp": int(time.time())
        }

        self.client.will_set(
            topic=self.availability_topic,
            payload=json.dumps(offline_payload),
            qos=1,
            retain=True
        )

        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message

        self.connected = False

    def connect(self):
        log(f"Connecting to MQTT broker at {self.host}:{self.port}")

        self.client.connect(
            host=self.host,
            port=self.port,
            keepalive=60
        )

        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.connected = True

            log("MQTT connected")

            self.client.subscribe(self.command_topic)

            log(f"Subscribed to {self.command_topic}")

            self.publish_availability_online()

        else:
            log(f"MQTT connection failed with rc={rc}")

    def on_disconnect(self, client, userdata, rc):
        self.connected = False

        if rc != 0:
            log("MQTT unexpectedly disconnected")
        else:
            log("MQTT disconnected")

    def on_message(self, client, userdata, message):
        topic = message.topic
        payload = message.payload.decode()

        log("MQTT message received")

        log(f"Topic: {topic}")

        log(f"Payload: {payload}")

    def publish_availability_online(self):
        payload = {
            "nodeId": self.node_id,
            "status": "online",
            "timestamp": int(time.time())
        }

        result = self.client.publish(
            topic=self.availability_topic,
            payload=json.dumps(payload),
            qos=1,
            retain=True
        )

        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            log(
                f"Availability published to "
                f"{self.availability_topic}"
            )
        else:
            log(
                f"Failed to publish availability to "
                f"{self.availability_topic}"
            )

    def publish_heartbeat(self):
        if not self.connected:
            log(
                "Skipping heartbeat publish: "
                "MQTT not connected"
            )
            return

        payload = {
            "nodeId": self.node_id,
            "timestamp": int(time.time()),
            "status": "online"
        }

        result = self.client.publish(
            topic=self.heartbeat_topic,
            payload=json.dumps(payload),
            qos=1,
            retain=False
        )

        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            log(
                f"Heartbeat published to "
                f"{self.heartbeat_topic}"
            )
        else:
            log(
                f"Failed to publish heartbeat to "
                f"{self.heartbeat_topic}"
            )

    def disconnect(self):
        log("Disconnecting MQTT client")

        offline_payload = {
            "nodeId": self.node_id,
            "status": "offline",
            "timestamp": int(time.time())
        }

        self.client.publish(
            topic=self.availability_topic,
            payload=json.dumps(offline_payload),
            qos=1,
            retain=True
        )

        self.client.loop_stop()
        self.client.disconnect()