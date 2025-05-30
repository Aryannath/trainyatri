from context import station_codes, class_types, quota_types
from dotenv import load_dotenv
import os

def get_station_codes() -> dict:
    return station_codes

def get_class_types() -> dict:
    return class_types

def get_quota_types() -> dict:
    return quota_types

def get_rail_api_key() -> str:
    return os.getenv("RAIL_API_KEY", "")
