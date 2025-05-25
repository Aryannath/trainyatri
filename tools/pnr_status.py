from fastmcp import Context

async def get_pnr_status(pnr: str, ctx:Context) -> str:
    station_data = await ctx.read_resource("data://stations")
    # Replace with actual CRIS API call
    return f"Mocked PNR status for {pnr}"

