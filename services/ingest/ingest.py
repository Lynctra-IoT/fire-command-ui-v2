import asyncio, json, os
from dotenv import load_dotenv
import serial_asyncio
import aiohttp
import paho.mqtt.client as mqtt

load_dotenv()
SERIAL_PORT = os.getenv("SERIAL_PORT", "/dev/ttyUSB0")
BAUD        = int(os.getenv("BAUD", 9600))
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
MQTT_HOST   = os.getenv("MQTT_HOST", "localhost")

# very naive Odyssey decoder: each line plain JSON already
async def process_line(line: str, http_sess, mqtt_cli):
    try:
        payload = json.loads(line.strip())
    except Exception:
        return
    # REST
    await http_sess.post(f"{BACKEND_URL}/api/v1/events/", json=payload)
    # MQTT optional
    mqtt_cli.publish("firepanel/events", json.dumps(payload))

async def main():
    mqtt_cli = mqtt.Client()
    mqtt_cli.connect(MQTT_HOST, 1883, 60)
    mqtt_cli.loop_start()

    async with aiohttp.ClientSession() as http_sess:
        # remove serial loop, just sleep and wait for external publish
        print("Ingest running with no serial port (SERVER MODE).")
        while True:
            await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
