from fastmcp import Context
import requests
from typing import List, Dict, Any

async def get_live_station_status(station_code: str, hours: int, ctx: Context):
   
    api_key = ctx.read_resource("data://rail_api_key")
    
    url = f"http://indianrailapi.com/api/v2/LiveStation/apikey/{api_key}/StationCode/{station_code}/hours/{hours}/"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("ResponseCode") == "200" and data.get("Status") == "SUCCESS":
            result = []
            trains = data.get("Trains", [])

            # Process each train's information
            for train in trains:
                result.append({
                    "type": "train_status",
                    "name": train.get("Name", "Unknown"),
                    "number": train.get("Number", "Unknown"),
                    "source": train.get("Source", "Unknown"),
                    "destination": train.get("Destination", "Unknown"),
                    "schedule": {
                        "arrival": train.get("ScheduleArrival", "-"),
                        "departure": train.get("ScheduleDeparture", "-"),
                        "halt": train.get("Halt", "-")
                    },
                    "expected": {
                        "arrival": train.get("ExpectedArrival", "-"),
                        "departure": train.get("ExpectedDeparture", "-")
                    },
                    "delay": {
                        "arrival": train.get("DelayInArrival", "-"),
                        "departure": train.get("DelayInDeparture", "-")
                    }
                })

            return result

        return [{
            "type": "error",
            "message": f"API Error: {data.get('Message', 'Unknown error')}"
        }]

    except Exception as e:
        return [{
            "type": "error",
            "message": f"Error fetching station status: {str(e)}"
        }]