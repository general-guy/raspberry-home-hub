import time
from logger import log

def heartbeat_loop():
    while True:
        log("Hub heartbeat alive")
        time.sleep(5)