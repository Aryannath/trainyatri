from fastmcp import Context

async def get_live_status(train_no: str, date: str, ctx: Context) -> str:
    station_data = await ctx.read_resource("data://stations")
    return f"Mocked live status for train {train_no} on {date}"



