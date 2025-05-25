from fastmcp import FastMCP
from tools.pnr_status import get_pnr_status
from tools.fare_enquiry import get_fare
from tools.seat_availability import check_seat_availability
from tools.train_schedule import get_train_schedule
from tools.live_status import get_live_status
from tools.station_search import search_station
from prompts import default_prompt, error_prompt, fallback_prompt
from resources import get_station_codes, get_class_types, get_quota_types

mcp = FastMCP(
    name="TrainYatri",
    instructions="You are a helpful assistant focused on Indian Railways information. You can help with train schedules, PNR status, and fare enquiries."
)

# Register tools
mcp.tool(
    name="get_pnr_status",
    description="Gets PNR status for a given PNR number"
)(get_pnr_status)
mcp.tool(
    name="get_fare",
    description="Gets fare info for a train route, class, and quota"
)(get_fare)
mcp.tool(
    name="check_seat_availability",
    description="Checks seat availability on a train between two stations for a given date"
)(check_seat_availability)

mcp.tool(
    name="get_train_schedule",
    description="Gets full schedule for a given train number"
)(get_train_schedule)

mcp.tool(
    name="get_live_status",
    description="Gets live running status for a Station"
)(get_live_status)

mcp.tool(
    name="search_station",
    description="Searches for stations by name or code"
)(search_station)

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

# if __name__ == "__main__":
#     mcp.run(transport="stdio")

if __name__ == "__main__":
    mcp.run(transport="sse", host="127.0.0.1", port=8000)
