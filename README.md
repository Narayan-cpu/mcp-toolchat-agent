

# 🧠 Intelligent Memory-Enabled Agent with LangChain, Groq, and MCP Integration

## 📘 Project Title:  **"MCP Toolchat Agent"**

**"Tool-Augmented Conversational AI using LangChain, MCP, and Groq’s LLaMA 3 LLM"**


## 📝 Abstract

This project presents an interactive, memory-enabled conversational assistant that is capable of **reasoning, information retrieval, and tool usage** by integrating three powerful systems:

* **LangChain** – An open-source framework for building context-aware LLM agents.
* **Groq** – A high-performance LLM provider using **LLaMA 3 70B**, offering low-latency, high-throughput inference.
* **MCP (Model context protocol)** – A protocol designed to allow LLMs to interact with external tools in a structured, safe, and extensible way.

The agent supports **live tool usage** such as DuckDuckGo search, browser automation, and API-based queries, while maintaining **conversational memory** for contextual reasoning.

---

## 🎯 Objective

To build a **modular, extensible, and memory-capable AI assistant** that:

* Accepts user inputs in natural language.
* Retains contextual memory across turns.
* Dynamically chooses when to invoke external tools like search engines, web browsers, or data APIs.
* Returns meaningful, processed responses combining LLM reasoning and real-world data.

---

## 🛠️ Key Technologies

| Technology       | Role                                                        |
| ---------------- | ----------------------------------------------------------- |
| Python (asyncio) | Event-driven execution for responsive chat loop             |
| LangChain        | LLM orchestration and agent framework                       |
| Groq             | Ultra-fast inference for LLaMA 3 (70B) model                |
| MCP              | Tool interface protocol for extending LLM capabilities      |
| dotenv           | Secure API key management                                   |
| npx (Node.js)    | Tool server initialization (DuckDuckGo, Airbnb, Playwright) |

---

## 🧩 Introduction to MCP

Traditional LLMs are excellent at **reasoning and generation**, but lack the ability to:

* Access **live data** (news, weather, search, etc.)
* Interact with **web interfaces**
* Call **external systems or APIs**

To bridge this gap, **LangChain introduced MCP**, a secure protocol enabling LLMs to **invoke external tool servers**. Each server performs a dedicated task and responds with structured output.

---

## 🔍 Use Case

Imagine a user types:

> “Book a stay in Goa for this weekend with sea view.”

* The agent uses **context memory** to retain date and location.
* Recognizes the task as a **tool-appropriate task** (Airbnb).
* Invokes `@openbnb/mcp-server-airbnb` to fetch listings.
* Processes the structured JSON response using LLaMA-3 to provide human-like suggestions.

---

```mermaid
flowchart TD
    A[User Input] -->|Text| B[MCP Agent (LangChain)]
    B --> C[LLM: ChatGroq (LLaMA3-70B)]
    B --> D[MCP Client]
    D --> E1[DuckDuckGo Tool Server]
    D --> E2[Playwright Browser Server]
    D --> E3[Airbnb API Server]
    E1 --> D
    E2 --> D
    E3 --> D
    D --> B
    B -->|Natural Language| A
```

---

## 📁 Project Files

| File               | Description                                               |
| ------------------ | --------------------------------------------------------- |
| `main.py`          | Main async chat script with memory-enabled agent loop     |
| `mcp_use.py`       | Custom module for initializing `MCPAgent` and `MCPClient` |
| `browser_mcp.json` | MCP tool configuration                                    |
| `.env`             | API keys for secure access (e.g., GROQ\_API\_KEY)         |
| `README.md`        | Full project documentation                                |

---

## 🧠 Code Explanation

### `main.py`

```python
async def run_memory_chat():
    ...
    client = MCPClient.from_config_file("browser_mcp.json")
    llm = ChatGroq(model="llama3-70b-8192")
    agent = MCPAgent(llm=llm, client=client, memory_enabled=True)
```

* Loads configuration and initializes Groq-backed LangChain LLM.
* Creates an `MCPAgent` that can reason, remember, and use tools.

```python
while True:
    user_input = input("You: ")
    ...
    response = await agent.run(user_input)
```

* Event loop reads user input.
* Delegates reasoning and tool use to the agent.
* Supports `exit` and `clear` commands for user control.

---

## 🔧 MCP Tool Configuration (browser\_mcp.json)

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "airbnb": {
      "command": "npx",
      "args": ["-y", "@openbnb/mcp-server-airbnb"]
    },
    "duckduckgo-search": {
      "command": "npx",
      "args": ["-y", "duckduckgo-mcp-server"]
    }
  }
}
```

* You can plug-and-play any MCP-compatible tool.
* Each tool can be invoked independently depending on user intent.

---

## 🚀 How to Run

### 1. Clone and set up environment

```bash
git clone https://github.com/Narayan-CPU/tool-agent-groq.git
cd tool-agent-groq
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Add your `.env` file

```dotenv
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Run the agent

```bash
python main.py
```

---

## 🔍 Research Insights

This project demonstrates a **hybrid AI agent design** where:

* **LLMs act as orchestrators**, not just responders.
* **External microservices enhance factual accuracy**.
* **Tool-use is conditional and reasoned**, not fixed or rule-based.

This aligns with current research in:

* **Tool-augmented LLMs**
* **Multi-agent collaboration**
* **LLM plugins and observability**

---

## 📈 Future Enhancements

* ✅ Add voice interface using `SpeechRecognition` or `Whisper`.
* ✅ Add database-backed memory persistence.
* ✅ Build your own custom MCP tool (e.g., for weather, maps).
* ✅ Deploy as a web app with FastAPI + WebSocket.

---

## 📄 Conclusion

This project is a solid prototype for **next-gen AI interfaces** – combining the cognitive power of LLMs with the functional utility of tools. With Groq for speed, LangChain for structure, and MCP for extensibility, you now have a scalable foundation for:

* Personal assistants
* Task automation bots
* Intelligent API wrappers
* Custom research agents

---



