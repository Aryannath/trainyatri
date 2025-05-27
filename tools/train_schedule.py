from fastmcp import Context
import requests
from typing import List, Dict, Any


async def get_train_schedule(train_no: str, ctx: Context):

    api_key = ctx.read_resource("data://rail_api_key")
    result = []

    url = f"https://indianrailapi.com/api/v2/TrainSchedule/apikey/{api_key}/TrainNumber/{train_no}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("ResponseCode") == "200" and data.get("Status") == "SUCCESS":
            result.append({
                "type": "train_info",
                "train_number": train_no
            })

            # Add station schedule information
            route = data.get("Route", [])
            for station in route:
                result.append({
                    "type": "station_schedule",
                    "serial_no": station.get("SerialNo"),
                    "station_code": station.get("StationCode"),
                    "station_name": station.get("StationName"),
                    "arrival_time": station.get("ArrivalTime"),
                    "departure_time": station.get("DepartureTime"),
                    "distance": station.get("Distance")
                })
        else:
            result.append({
                "type": "error",
                "message": f"API Error: {data.get('Message', 'Unknown error')}"
            })

    except Exception as e:
        result.append({
            "type": "error",
            "message": f"Error fetching train schedule: {str(e)}"
        })

    return result