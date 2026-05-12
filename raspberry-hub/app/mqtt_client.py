import json
import time

import paho.mqtt.client as mqtt

from logger import log


class MQTTClient:
    def __init__(self, config: dict):
        self.node_id = config["nodeId"]

        self.host = config["mqtt"]["host"]
        self.port = config["mqtt"]["port"]

        self.client = mqtt.Client(
            client_id=self.node_id,
            clean_session=True
        )

        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect

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
        else:
            log(f"MQTT connection failed with rc={rc}")

    def on_disconnect(self, client, userdata, rc):
        self.connected = False

        if rc != 0:
            log("MQTT unexpectedly disconnected")
        else:
            log("MQTT disconnected")

    def publish_heartbeat(self):
        if not self.connected:
            log("Skipping heartbeat publish: MQTT not connected")
            return

        topic = f"rhh/{self.node_id}/heartbeat"

        payload = {
            "nodeId": self.node_id,
            "timestamp": int(time.time()),
            "status": "online"
        }

        result = self.client.publish(
            topic=topic,
            payload=json.dumps(payload),
            qos=1
        )

        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            log(f"Heartbeat published to {topic}")
        else:
            log(f"Failed to publish heartbeat to {topic}")

    def disconnect(self):
        log("Disconnecting MQTT client")

        self.client.loop_stop()
        self.client.disconnect()