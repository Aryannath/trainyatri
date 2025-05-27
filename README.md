# 🚂 TrainYatri Model Context Protocol Server

A sophisticated implementation of Model Context Protocol (MCP) for Indian Railways information systems. TrainYatri leverages advanced AI models with contextual awareness to provide intelligent railway information services through a well-structured API interface.

## 🌟 Features

- **AI-Powered Railway Information**
  - Context-aware train status tracking
  - Intelligent PNR status interpretation
  - Smart schedule analysis
  - Predictive seat availability
  - Dynamic fare calculations
  - Real-time station monitoring
  - Natural language station search

- **Model Context Protocol Implementation**
  - Built on FastMCP framework for model-context interactions
  - Context-aware tool selection and execution
  - Intelligent prompt management
  - Structured context handling
  - Advanced error recovery
  - SSE (Server-Sent Events) for real-time updates


## 📁 Project Structure

```
trainyatri/
├── tools/                  # Core functionality modules
│   ├── fare_enquiry.py    # Train fare lookups
│   ├── live_status.py     # Real-time train tracking
│   ├── pnr_status.py      # PNR status checking
│   ├── seat_availability.py# Seat availability checks
│   ├── station_search.py  # Station search functionality
│   ├── station_status.py  # Live station monitoring
│   └── train_schedule.py  # Train schedule retrieval
├── models/                 # Data models
├── resources.py           # Resource management
├── context.py            # Context definitions
├── prompts.py           # AI prompt templates
├── main.py              # Server entry point
└── requirements.txt     # Dependencies
```

## 🧠 Model Context Architecture

```
Context Layer:
├── Station Context   # Station codes and metadata
├── Class Context    # Train class definitions
├── Quota Context   # Booking quota rules
└── API Context    # Railway API integration

Model Layer:
├── Prompt Systems   # Context-aware prompting
└── Response Models  # Structured output generation

Protocol Layer:
├── Tool Registry   # Railway information tools
├── Context Handlers # State management
└── Event Streams   # Real-time updates
```

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd trainyatri
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment:**
   Create a `.env` file with:
   ```
   RAIL_API_KEY=your_api_key
   MODEL_API_KEY=your_openrouter_key
   ```

4. **Run the server:**
   ```bash
   python main.py
   ```
   Server runs at `http://127.0.0.1:8000`

## 🔧 Available Tools

- `get_pnr_status`: Check PNR status
- `get_fare`: Retrieve train fare details
- `check_seat_availability`: Check seat availability
- `get_train_schedule`: Get complete train schedules
- `get_live_status`: Track trains in real-time
- `search_station`: Search railway stations
- `get_live_station_status`: Monitor station status

## 🤖 AI Integration

- Attach to any LLM Client
- Custom prompt templates for various scenarios
- Context-aware responses
- Fallback handling for edge cases

## ⚙️ Configuration

- VSCode integration via `mcp.json`
- Environment-based configuration
- Flexible resource management
- Quota and class type definitions


## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.