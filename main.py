from fastmcp import FastMCP
from tools.pnr_status import get_pnr_status
from tools.fare_enquiry import get_fare
from models.openrouter import model_client
from tools.seat_availability import check_seat_availability
from tools.train_schedule import get_train_schedule
from tools.live_status import get_live_status


mcp = FastMCP(
    name="TrainYatri",
    instructions="You are TrainYatri, an Indian Railways assistant. Help users with train and PNR queries.",
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
    description="Gets live running status for a train on a given date"
)(get_live_status)

if __name__ == "__main__":
    mcp.run(transport="stdio")
