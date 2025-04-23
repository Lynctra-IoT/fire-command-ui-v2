from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "YOUR_DEFAULT_SECRET_KEY")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./fire_command_v2.db")
    MQTT_BROKER: str = os.getenv("MQTT_BROKER", "localhost")
    MQTT_PORT: int = int(os.getenv("MQTT_PORT", 1883))

settings = Settings()
