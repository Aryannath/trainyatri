# 🚄 TrainYatri: AI-Powered Indian Railways Assistant with Model Context Protocol

**TrainYatri** is a powerful  **Model Context Protocol (MCP)** server tailored for Indian Railways. Built using the `indianrailapi` and `FastMCP` framework, it seamlessly integrates real-time railway data leveraging **LLMs(Large Language Models)** enabling users to track trains, search stations, check PNRs, and more all through intelligent AI tools within a clean, extensible design.

---

## 🌐 What is the Model Context Protocol (MCP)?

The **Model Context Protocol (MCP)** is an open standard developed by Anthropic that standardizes how applications provide context to LLMs.  Think of MCP as the "USB-C port" for AI applications, offering a universal interface for connecting AI models to various data sources and tools.&#x20;

MCP enables developers to build secure, two-way connections between their data sources and AI-powered tools.  It allows AI models to connect directly with external data sources, enabling them to read from and write to connected applications.&#x20;

---

## ✨ Key Features

### 🎛️ AI + MCP in Action

* **Live Train Tracking**: Get context-aware real-time train positions.
* **PNR Status Checks**: Receive natural language interpretations of PNR statuses.
* **Full Schedule Retrieval**: Access structured station data for train schedules.
* **Seat Availability**: Obtain insights with quota/class breakdowns.
* **Fare Enquiries**: Leverage external APIs for fare information.
* **Autocomplete Station Search**: Utilize fuzzy matching for station searches.
* **Live Station Status**: Get updates on nearby train arrivals and departures.

### 🤖 Built on FastMCP

* **Multi-tool Support**: Automatically route user queries to appropriate tools.
* **Prompt Fallback & Error Recovery**: Ensure natural responses even in ambiguous scenarios.
* **Clean Context Management**: Maintain structured context for LLMs (stations, quotas, etc.).
* **Structured Tool I/O**: Designed for AI agents & Inspector.
* **Flexible Deployment**: Easily run with `stdio` , `sse` or `streamable-http` transport.

---

## 🧱 Project Structure

```bash
trainyatri/
├── tools/                 # Core logic per feature
│   ├── fare_enquiry.py
│   ├── live_status.py
│   ├── pnr_status.py
│   ├── seat_availability.py
│   ├── station_search.py
│   ├── station_status.py
│   └── train_schedule.py
├── prompts.py             # Prompt logic
├── resources.py           # Shared resources (station codes, quotas, etc.)
├── context.py             # Context-aware extensions
├── main.py                # MCP server entry point
├── .env                   # Secrets and API keys (not committed)
├── requirements.txt       # Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/aryan/trainyatri.git
cd trainyatri
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys

Create a `.env` file:

```
RAIL_API_KEY=your_indianrailapi_key
MODEL_API_KEY=your_openrouter_key
```

### 4. Start the MCP Server

```bash
python main.py
```

Or, run with Inspector enabled:

```bash
fastmcp dev main.py
```

---

## 🧰 Tools Registered

| Tool                      | Description                           |
| ------------------------- | ------------------------------------- |
| `get_pnr_status`          | Get PNR status                        |
| `get_fare`                | Retrieve train fare                   |
| `check_seat_availability` | Seat availability by quota/class/date |
| `get_train_schedule`      | Train schedule lookup                 |
| `get_live_status`         | Real-time train position              |
| `get_live_station_status` | See trains at a given station         |
| `search_station`          | Autocomplete railway station names    |

---

## 🧑‍💻 How Users Interact with TrainYatri
### 🔍 Example 1: PNR Status Check

> **User asks:** “Can you tell me the status of PNR 8701234567?”
> **What happens:**
> The MCP client triggers the `get_pnr_status` tool on the TrainYatri server → fetches live data from Indian Railways → and the LLM replies:
> **“Your train is confirmed. Coach S3, seat 42. Boarding at Pune Junction on June 3rd at 18:40.”**

---

### 🛤️ Example 2: Track a Live Train

> **User asks:** “Where is train 12951 right now?”
> **What happens:**
> The MCP client invokes the `get_live_status` tool → receives real-time train coordinates → and the LLM responds:
> **“Train 12951 is currently between Vadodara and Surat, running 10 minutes late.”**

---

### 🪑 Example 3: Check Seat Availability

> **User asks:** “Any 3AC seats from Mumbai to Jaipur on June 15?”
> **What happens:**
> The `check_seat_availability` tool runs → parses availability by date/quota/class → and the LLM replies:
> **“Yes, there are 16 seats available in 3AC on train 12955 under the General Quota.”**

---

## 🛠️ VS Code & Development Setup

This project includes a `.vscode` folder with recommended settings and launch configurations for a smooth developer experience.

* **Launch MCP Server**: Use the pre-configured launch tasks in VS Code to start the server directly (look for "Run MCP Server" or similar in the Run & Debug panel).
* **Environment Variables**: The `.env` file is automatically loaded if you use the VS Code Python extension.
* **Debugging**: Step through requests and tool logic with breakpoints in VS Code.

---

## 🔌 Integration & Client Connectivity

* **LLM Clients**: The MCP server exposes a 'stdio' transport compatible with clients like **Claude Desktop**, and **GitHub Copilot** (with custom endpoints).
* Use the mcp.json file to configure any client to use the server.
---

## 🧠 How the MCP Server Works

* **FastMCP Framework**: Handles routing, tool registration, and context management for LLM-based workflows.
* **Tool Registration**: Each feature (PNR, fare, etc.) is a tool in `/tools` and auto-registered on startup.
* **Context & Resources**: Shared data (station codes, quotas, etc.) is loaded at startup and injected into tool logic as needed.
* **Prompt Handling**: Custom prompts and error handling ensure robust, natural responses even for ambiguous queries.
* **Extensibility**: Add new tools by creating a Python file in `/tools` and updating `main.py` if needed.

---

## 🔐 Security & Best Practices

* Store API keys in `.env`, not directly in code.
* Avoid leaking secrets in prompts/logs.
* Use `requests` instead of `httpx` for simplicity.

---

## 🤝 Contributions

Pull requests, suggestions, and bug reports are welcome. Drop a star ⭐ and fork away!
Or contact for any issue. 

---


