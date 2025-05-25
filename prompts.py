from fastmcp.prompts.prompt import Message, PromptMessage, TextContent


def default_prompt() -> PromptMessage:
    """Default system prompt for TrainYatri."""
    content = """You are a helpful assistant focused on Indian Railways information.
    You can help with train schedules, PNR status, and fare enquiries."""
    return PromptMessage(role="assistant", content=TextContent(type="text", text=content))


def error_prompt(error_type: str) -> PromptMessage:
    """Generates error message based on error type."""
    content = f"""I apologize, but I encountered an {error_type} error.
    Please check the information provided and try again.
    For PNR status: Ensure you provide a valid 10-digit PNR number.
    For train enquiries: Verify the train number and station codes."""
    return PromptMessage(role="assistant", content=TextContent(type="text", text=content))


def fallback_prompt() -> PromptMessage:
    """Fallback message when request cannot be handled."""
    content = """I understand you're asking about Indian Railways, but I'm not sure how to help with that specific request.
    I can assist you with:
    - Checking PNR status
    - Looking up train schedules
    - Checking seat availability
    - Getting fare information
    - Checking live train status
    Please rephrase your question using one of these options."""
    return PromptMessage(role="assistant", content=TextContent(type="text", text=content))