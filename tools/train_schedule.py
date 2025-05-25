from fastmcp import Context

async def get_train_schedule(train_no: str, ctx: Context) -> str:
    station_data = await ctx.read_resource("data://stations")
    return f"Mocked schedule for train {train_no}"