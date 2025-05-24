from fastmcp import Tool

def get_train_schedule(train_no: str) -> str:
    return f"Mocked train schedule for train {train_no}"

tool = Tool.from_function(
    func=get_train_schedule,
    name="get_train_schedule",
    description="Gets full schedule for a given train number"
)