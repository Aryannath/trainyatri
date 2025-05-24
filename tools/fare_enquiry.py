from fastmcp import Tool

def get_fare(train_no: str, source: str, dest: str, age: int, quota: str, cls: str) -> str:
    return f"Mocked fare enquiry for train {train_no} from {source} to {dest}"

tool = Tool.from_function(
    func=get_fare,
    name="get_fare",
    description="Gets fare info for a train route, class, and quota"
)
