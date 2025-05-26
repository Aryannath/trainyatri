from fastmcp import Context
import requests
from typing import List, Dict, Any

async def get_fare(train_no: str, source: str, destination: str, train_class: str, quota: str, ctx: Context):
    
    # Get API key from context
    api_key = ctx.read_resource("data://rail_api_key")
    
    # Construct API URL
    url = f"http://indianrailapi.com/api/v2/TrainFare/apikey/{api_key}/TrainNumber/{train_no}/From/{source}/To/{destination}/Quota/{quota}"

    try:
        # Make API request
        response = requests.get(url, timeout=10)
        data = response.json()

        # Check if request was successful
        if data.get("ResponseCode") == "200" and data.get("Status") == "SUCCESS":
            result = []
            
            # Add train information
            result.append({
                "type": "train_info",
                "train_number": data.get("TrainNumber"),
                "train_name": data.get("TrainName"),
                "from_station": data.get("From"),
                "to_station": data.get("To"),
                "distance": data.get("Distance"),
                "train_type": data.get("TrainType")
            })

            # Add fare information for each class
            fares = data.get("Fares", [])
            for fare in fares:
                result.append({
                    "type": "fare_info",
                    "class_name": fare.get("Name"),
                    "class_code": fare.get("Code"),
                    "fare": fare.get("Fare")
                })

            return result

        return [{
            "type": "error",
            "message": f"API Error: {data.get('Message', 'Unknown error')}"
        }]

    except requests.RequestException as e:
        return [{
            "type": "error",
            "message": f"Error fetching fare information: {str(e)}"
        }]