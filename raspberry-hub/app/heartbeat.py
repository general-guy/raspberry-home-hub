import time

from logger import log


def heartbeat_loop(mqtt_client, interval_seconds: int):
    while True:
        log("Hub heartbeat alive")

        mqtt_client.publish_heartbeat()

        time.sleep(interval_seconds)