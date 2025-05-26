from fastmcp import Context
import requests
from typing import List, Dict, Any


async def get_live_status(train_no: str, date: str, ctx: Context):

    API_URL = "http://indianrailapi.com/api/v2/livetrainstatus/apikey/{api_key}/trainnumber/{train_number}/date/{date}/"

    api_key = ctx.read_resource("data://rail_api_key")
    url = API_URL.format(api_key=api_key, train_number=train_no, date=date)

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("ResponseCode") != "200":
            return [{
                "type": "error",
                "message": f"API Error: {data.get('Message', 'Unknown error')}"
            }]

        result = []

        # Get current position
        current_station = data.get("CurrentStation", {})
        if current_station:
            result.append({
                "type": "current_position",
                "train_number": train_no,
                "station_name": current_station.get('StationName'),
                "station_code": current_station.get('StationCode'),
                "schedule_arrival": current_station.get('ScheduleArrival'),
                "actual_arrival": current_station.get('ActualArrival'),
                "delay": current_station.get('DelayInArrival')
            })

        # Get route information
        route = data.get("TrainRoute", [])
        if route:
            for station in route:
                result.append({
                    "type": "route_station",
                    "station_name": station.get("StationName", "Unknown"),
                    "station_code": station.get("StationCode", ""),
                    "schedule_arrival": station.get("ScheduleArrival", "-"),
                    "actual_arrival": station.get("ActualArrival", "-"),
                    "schedule_departure": station.get("ScheduleDeparture", "-"),
                    "actual_departure": station.get("ActualDeparture", "-"),
                    "delay": station.get("DelayInArrival", "-"),
                    "distance": station.get("Distance", "-"),
                    "day": station.get("Day", "0")
                })

        return result

    except Exception as e:
        return [{
            "type": "error",
            "message": f"Error fetching live train status: {str(e)}"
        }]
