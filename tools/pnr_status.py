from fastmcp import Tool

def get_pnr_status(pnr: str) -> str:
    # Replace with actual CRIS API call
    return f"Mocked PNR status for {pnr}"

tool = Tool.from_function(
    func=get_pnr_status,
    name="get_pnr_status",
    description="Returns PNR status info given a PNR number"
)

