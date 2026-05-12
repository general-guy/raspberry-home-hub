from logger import log
from heartbeat import heartbeat_loop

def main():
    log("Raspberry Home Hub starting...")
    heartbeat_loop()

if __name__ == "__main__":
    main()