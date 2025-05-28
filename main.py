from fastmcp import FastMCP
from tools.pnr_status import get_pnr_status
from tools.fare_enquiry import get_fare
from tools.seat_availability import check_seat_availability
from tools.train_schedule import get_train_schedule
from tools.live_status import get_live_status
from tools.station_search import search_station
from tools.station_status import get_live_station_status
from prompts import default_prompt, error_prompt, fallback_prompt
from resources import get_station_codes, get_class_types, get_quota_types, get_rail_api_key


mcp = FastMCP(
    name="TrainYatri",
    instructions="You are a helpful assistant focused on Indian Railways information. You can help with train schedules, PNR status, and fare enquiries.",
    
)

# Register tools
mcp.tool(
    name="get_pnr_status",
    description="Gets detailed PNR status including train info, passenger status, and booking details"
)(get_pnr_status)
mcp.tool(
    name="get_fare",
    description="Gets train fare details. Parameters required: \n"
                "- trainNumber: Train number (e.g., 12345)\n"
                "- stationFrom: Source station code (e.g., NDLS)\n" 
                "- stationTo: Destination station code (e.g., MMCT)\n"
                "- quota: Booking quota (GN=General, CK=Tatkal)"
)(get_fare)
mcp.tool(
    name="check_seat_availability",
    description="Gets seat availability for a train, Currently only GN-General available. Parameters required:\n"
                "- trainNumber: Train number (e.g., 12345)\n"
                "- stationFrom: Source station code (e.g., NDLS)\n"
                "- stationTo: Destination station code (e.g., MMCT)\n"
                "- date: Journey date in YYYYMMDD format\n"
                "- class: Travel class code (1A/2A/3A/SL etc.)\n"
                
)(check_seat_availability)

mcp.tool(
    name="get_train_schedule",
    description="Gets full schedule for a train with station-wise arrival/departure timings. Parameters required:\n"
                "- trainNumber: Train number (e.g., 12345)\n"
)(get_train_schedule)

mcp.tool(
    name="get_live_status",
    description="Gets live Train Status. Train number and date (YYYYMMDD format) required."
)(get_live_status)

mcp.tool(
    name="search_station",
    description="Searches for stations by name or code"
)(search_station)

mcp.tool(
    name="get_live_station_status",
    description="Gets live status of a station for a given Station Code (In capital letter) and hour 2 or 4 (ie; within 2 hrs. or 4 hrs.)."
)(get_live_station_status)

# Register prompts
mcp.prompt(
    name="default_prompt",
    description="Default system prompt for TrainYatri"
)(default_prompt)
mcp.prompt(
    name="error_prompt",
    description="Generates error message based on error type"
)(error_prompt)
mcp.prompt(
    name="fallback_prompt",
    description="Fallback message when request cannot be handled"
)(fallback_prompt)

# Register resources
mcp.resource("data://stations")(get_station_codes)
mcp.resource("data://class_types")(get_class_types)
mcp.resource("data://quota_types")(get_quota_types)
mcp.resource("config://RAIL_API_KEY")(get_rail_api_key)

if __name__ == "__main__":
    mcp.run(transport="stdio")

# if __name__ == "__main__":
#     mcp.run(transport="sse", host="127.0.0.1", port=8000)
