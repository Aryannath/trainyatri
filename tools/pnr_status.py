from models.openrouter import model_client

def get_pnr_status(pnr: str) -> str:
    # Example prompt to LLM: ask it to explain PNR status based on a mocked API response
    prompt = f"Explain the PNR status for PNR number {pnr}. The PNR is confirmed."
    
    response = model_client.chat.completions.create(
        model="gpt-4o-mini",  # or whatever model you want
        messages=[{"role": "user", "content": prompt}],
    )
    answer = response.choices[0].message.content
    return answer

# def get_pnr_status(pnr: str) -> str:
#     # Replace with actual CRIS API call
#     return f"Mocked PNR status for {pnr}"

