import requests
from fastmcp import Context


async def search_station(station_name: str, ctx: Context) -> str:
    # Retrieve the API key from the context configuration
    api_key = ctx.read_resource("data://rail_api_key")

    # Construct the API URL
    url = f"http://indianrailapi.com/api/v2/AutoCompleteStation/apikey/{api_key}/StationCodeOrName/{station_name}/"

    try:
        # Make the HTTP GET request
        response = requests.get(url)
        data = response.json()

        # Check if the response is successful
        if data.get("ResponseCode") == "200" and data.get("Status") == "SUCCESS":
            stations = data.get("Station", [])
            if not stations:
                return f"No stations found matching '{station_name}'."

            # Format the station information
            result_lines = []
            for station in stations:
                name_en = station.get("NameEn", "N/A")
                name_hn = station.get("NameHn", "N/A")
                code = station.get("StationCode", "N/A")
                lat = station.get("Latitude", "N/A")
                long = station.get("Longitude", "N/A")
                result_lines.append({
                    "name_en": name_en,
                    "name_hn": name_hn,
                    "code": code,
                    "latitude": lat,
                    "longitude": long
                })

            return result_lines
        else:
            return f"API returned an error: {data.get('Message', 'Unknown error')}"

    except requests.RequestException as e:
        return f"An error occurred while fetching station data: {str(e)}"
