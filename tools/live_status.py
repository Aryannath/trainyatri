from fastmcp import Tool

def get_live_status(train_no: str, date: str) -> str:
    return f"Mocked live status for train {train_no} on {date}"

tool = Tool.from_function(
    func=get_live_status,
    name="get_live_status",
    description="Gets live running status for a train on a given date"
)

