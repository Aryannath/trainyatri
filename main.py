from fastmcp import FastMCP
from tools.pnr import get_pnr_status
from tools.train_route import get_train_route

mcp = FastMCP(name="TrainYatri", instructions="Indian Railways MCP agent.")

# Register tools
mcp.tool(get_pnr_status)
mcp.tool(get_train_route)

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8000)
