from fastmcp import FastMCP
from tools.pnr_status import get_pnr_status
from tools.fare_enquiry import get_fare
from models.openrouter import model_client


mcp = FastMCP(
    name="TrainYatri",
    instructions="You are TrainYatri, an Indian Railways assistant. Help users with train and PNR queries.",
)

# Register tools
mcp.tool( name="get_pnr_status", description="Returns PNR status for a given PNR number")(get_pnr_status)
mcp.tool(name="get_fare",description="Gets fare info for a train route, class, and quota")(get_fare)

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8000)
