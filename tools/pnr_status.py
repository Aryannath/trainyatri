import requests
from fastmcp import Context
from typing import List, Dict, Any

async def get_pnr_status(pnr: str, ctx: Context):
    
    # Get API key from resources
    api_key = ctx.read_resource("data://rail_api_key")
    
    # Construct API URL
    url = f"http://indianrailapi.com/api/v2/PNRCheck/apikey/{api_key}/PnrNumber/{pnr}/"

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
                "pnr": pnr,
                "train_name": data.get('TrainName', 'N/A'),
                "train_number": data.get('TrainNumber', 'N/A'),
                "journey_class": data.get('JourneyClass', 'N/A'),
                "from_station": data.get('From', 'N/A'),
                "to_station": data.get('To', 'N/A'),
                "journey_date": data.get('JourneyDate', 'N/A')
            })
            
            # Add passenger information
            passengers = data.get('Passangers', [])
            for idx, passenger in enumerate(passengers, 1):
                result.append({
                    "type": "passenger_info",
                    "passenger_no": idx,
                    "booking_status": passenger.get('BookingStatus', 'N/A'),
                    "current_status": passenger.get('CurrentStatus', 'N/A')
                })
            
            return result
        else:
            return [{
                "type": "error",
                "message": f"Error checking PNR: {data.get('Message', 'Unknown error')}"
            }]

    except requests.RequestException as e:
        return [{
            "type": "error",
            "message": f"Error fetching PNR status: {str(e)}"
        }]

