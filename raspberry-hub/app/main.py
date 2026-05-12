import json

from logger import log
from heartbeat import heartbeat_loop
from mqtt_client import MQTTClient


SETTINGS_PATH = "config/settings.json"


def load_config():
    with open(SETTINGS_PATH, "r") as file:
        return json.load(file)


def main():
    log("Raspberry Home Hub starting...")

    config = load_config()

    mqtt_client = MQTTClient(config)

    try:
        mqtt_client.connect()

        heartbeat_loop(
            mqtt_client=mqtt_client,
            interval_seconds=config["heartbeatIntervalSeconds"]
        )

    except KeyboardInterrupt:
        log("Keyboard interrupt received")

    finally:
        mqtt_client.disconnect()

        log("Raspberry Home Hub stopped")


if __name__ == "__main__":
    main()