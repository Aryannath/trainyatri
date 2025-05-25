from fastmcp import Context


async def check_seat_availability(train_no: str, date: str, source: str, dest: str, ctx: Context) -> str:
    station_data = await ctx.read_resource("data://stations")
    return f"Mocked seat availability for train {train_no} on {date} from {source} to {dest}"

