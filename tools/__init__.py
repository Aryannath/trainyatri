from .pnr_status import tool as pnr_status_tool
from .seat_availability import tool as seat_availability_tool
from .train_schedule import tool as train_schedule_tool
from .fare_enquiry import tool as fare_enquiry_tool
from .live_status import tool as live_status_tool

TOOLS = [
    pnr_status_tool,
    seat_availability_tool,
    train_schedule_tool,
    fare_enquiry_tool,
    live_status_tool
]

