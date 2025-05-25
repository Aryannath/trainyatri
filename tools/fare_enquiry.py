from fastmcp import Context

async def get_fare(train_no: str, source: str, destination: str, train_class: str, quota: str, ctx: Context) -> str:
    station_data = await ctx.read_resource("data://stations")
    class_data = await ctx.read_resource("data://class_types")
    quota_data = await ctx.read_resource("data://quota_types")
    
    return f"Mocked fare for train {train_no} from {source} to {destination}"


