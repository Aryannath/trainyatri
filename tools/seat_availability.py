from fastmcp import Tool

def check_seat_availability(train_no: str, date: str, source: str, dest: str) -> str:
    return f"Mocked seat availability for train {train_no} on {date} from {source} to {dest}"

tool = Tool.from_function(
    func=check_seat_availability,
    name="check_seat_availability",
    description="Checks seat availability on a train between two stations for a given date"
)
