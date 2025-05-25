from fastmcp import Context
import requests

API_KEY = "9df253eb2be25faddff8fb4cefbf4c8a"
API_URL = "http://indianrailapi.com/api/v2/LiveStation/apikey/{api_key}/StationCode/{station_code}/hours/{hours}/"

def get_live_status(station_code: str, hours: int, ctx: Context) -> str:
    # Retrieve station data if needed
    station_data = ctx.read_resource("data://stations")

    # Format the API URL
    url = API_URL.format(api_key=API_KEY, station_code=station_code.upper(), hours=hours)

    try:
        response = requests.get(url)
        data = response.json()
        print(data)
    except Exception as e:
        return f"Error fetching live station data: {str(e)}"

    if data.get("ResponseCode") != "200":
        
        return f"API Error: {data.get('Message', 'Unknown error')}"

    trains = data.get("Trains", [])
    if not trains:
        return f"No trains found arriving at {station_code.upper()} in the next {hours} hours."

    result_lines = [f"Live trains arriving at {station_code.upper()} in the next {hours} hours:"]
    for train in trains:
        name = train.get("Name", "Unknown")
        number = train.get("Number", "Unknown")
        expected_arrival = train.get("ExpectedArrival", "N/A")
        delay = train.get("DelayInArrival", "N/A")
        result_lines.append(f"- {name} ({number}): Expected Arrival: {expected_arrival}, Delay: {delay}")

    return "\n".join(result_lines)
