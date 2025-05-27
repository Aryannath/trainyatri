from fastmcp import Context
import requests
from typing import List, Dict, Any


async def check_seat_availability(train_no: str, date: str, source: str, dest: str, train_class: str, ctx: Context) :
    
    api_key = ctx.read_resource("data://rail_api_key")
    result = []

    url = f"https://indianrailapi.com/api/v2/SeatAvailability/apikey/{api_key}/TrainNumber/{train_no}/From/{source}/To/{dest}/Date/{date}/Quota/GN/Class/{train_class}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("ResponseCode") == "200" and data.get("Status") == "SUCCESS":
            # Add train and class information
            result.append({
                "type": "availability_info",
                "train_number": data.get("TrainNo"),
                "class_code": data.get("ClassCode"),
                "quota": data.get("Quota"),
                "from_station": data.get("From"),
                "to_station": data.get("To")
            })

            # Add availability for different dates
            availabilities = data.get("Availability", [])
            for avail in availabilities:
                result.append({
                    "type": "date_availability",
                    "class_code": train_class,
                    "journey_date": avail.get("JourneyDate"),
                    "availability": avail.get("Availability"),
                    "confirmation_chance": avail.get("Confirm")
                })
        else:
            result.append({
                "type": "error",
                "message": f"API Error: {data.get('Message', 'Unknown error')}"
            })

    except Exception as e:
        result.append({
            "type": "error",
            "message": f"Error checking availability: {str(e)}"
        })

    return result
