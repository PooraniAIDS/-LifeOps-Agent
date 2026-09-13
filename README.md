# 🧠 LifeOps Agent

### AI-Powered Personal Decision-Support Assistant

LifeOps Agent is an intelligent AI assistant that helps users make practical decisions in everyday situations.

Instead of simply answering questions, the agent **understands the situation, decides which tools are required, executes them autonomously, combines the results, and provides a practical recommendation.**

> **Situation → Analyze → Decide → Recommend**

---

## ✨ Features

* 🤖 AI-powered autonomous decision making
* 🧩 Function/tool calling
* 🔄 Multi-tool execution
* 🔗 Tool-result chaining
* 🕐 Current time retrieval
* 📅 Future and past date calculation
* 💰 Expense and balance calculation
* 🧠 Budget-based decision recommendations
* 💬 Interactive Gradio web interface
* 🔐 Secure API key management using environment variables
* 📦 Modular Python project structure

---

## 🛠️ Agent Tools

| Tool             | Function                                              | Purpose                                         |

| 🕐 Time Tool     | `get_current_time()`                                  | Returns the current local time                  |
| 📅 Date Tool     | `calculate_date(days)`                                | Calculates a future or past date                |
| 💰 Expense Tool  | `calculate_expense(income, expenses)`                 | Calculates total expenses and remaining balance |
| 🧠 Decision Tool | `make_budget_decision(remaining_balance, event_days)` | Generates a practical budget recommendation     |

The agent decides **which tool or combination of tools** should be used based on the user's request.

---

## 🧩 How It Works

LifeOps follows an agent-based workflow:

```text
                    👤 USER
                       │
                       ▼
              🧠 LIFEOPS AGENT
                       │
                       ▼
                      LLM
                       │
              ┌────────┴────────┐
              │  Tool Selection │
              └────────┬────────┘
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   🕐 Time Tool   📅 Date Tool   💰 Expense Tool
        │              │              │
        └──────────────┼──────────────┘
                       │
                       ▼
              🧠 Decision Tool
                       │
                       ▼
               Agent Reasoning
                       │
                       ▼
             💡 Recommendation
```

The agent does **not** blindly execute every tool.

It analyzes the user's request and chooses the tools that are actually required.

---

## 🔄 Multi-Tool Reasoning

LifeOps can use multiple tools within a single request.

### Example

**User:**

> I have ₹5000 and my expenses are ₹500, ₹300 and ₹700. I have an important event 10 days from now. Tell me the event date, how much money I will have left, what time it is now, and give me a practical recommendation.

The agent can autonomously:

1. 🕐 Get the current time
2. 📅 Calculate the event date
3. 💰 Calculate total expenses and remaining balance
4. 🧠 Analyze the remaining budget and event timeframe
5. 💡 Generate a practical recommendation

This demonstrates **multi-tool agent behavior and tool-result chaining**.

---

## 💬 Example Queries

```text
What time is it now?
```

```text
What date will it be 15 days from today?
```

```text
I have ₹5000 and my expenses are ₹500, ₹300 and ₹700.
How much money will I have left?
```

```text
I have ₹5000 and my expenses are ₹500, ₹300 and ₹700.
I have an important event 10 days from now.
Tell me the event date, remaining money and give me a recommendation.
```

```text
I have ₹3000 left and an event is 2 days away.
Should I spend more money?
```

---

## 📁 Project Structure

```text
LifeOps-Agent/
│
├── tools/
│   ├── __init__.py
│   ├── time_tool.py
│   ├── date_tool.py
│   ├── expense_tool.py
│   └── decision_tool.py
│
├── agent.py
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

### File Description

| File               | Description                                                        |
| ------------------ | ------------------------------------------------------------------ |
| `agent.py`         | Core AI agent, tool definitions, tool execution and reasoning loop |
| `app.py`           | Gradio web application                                             |
| `time_tool.py`     | Current time functionality                                         |
| `date_tool.py`     | Date calculation functionality                                     |
| `expense_tool.py`  | Expense and balance calculations                                   |
| `decision_tool.py` | Budget decision and recommendation logic                           |
| `requirements.txt` | Python dependencies                                                |
| `.env`             | Stores the API key locally                                         |
| `.gitignore`       | Prevents sensitive/unnecessary files from being committed          |

---

## 💻 Tech Stack

### Programming Language

* Python

### AI / LLM

* Groq API
* OpenAI GPT-OSS 120B

### Interface

* Gradio

### Libraries

* `groq`
* `python-dotenv`
* `gradio`

### Development Tools

* VS Code
* Git
* GitHub

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/PooraniAIDS/-LifeOps-Agent.git
```

### 2. Navigate to the project

```bash
cd -LifeOps-Agent
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file in the project root:

```text
GROQ_API_KEY=your_groq_api_key_here
```

The API key should **never be committed to GitHub**.

The project already includes `.env` in `.gitignore`.

---

## ▶️ Running the Application

Start the Gradio application:

```bash
python app.py
```

After launching, Gradio will provide a local URL similar to:

```text
http://127.0.0.1:7860
```

Open the URL in your browser and start interacting with LifeOps Agent.

---

## 🧪 Testing Individual Tools

Each tool can also be tested independently.

### Time Tool

```bash
python tools/time_tool.py
```

### Date Tool

```bash
python tools/date_tool.py
```

### Expense Tool

```bash
python tools/expense_tool.py
```

### Decision Tool

```bash
python tools/decision_tool.py
```

---

## 🎯 Use Cases

LifeOps can be extended to support everyday decision-making scenarios such as:

* 💰 Personal budgeting
* 🛍️ Purchase decisions
* 📅 Event planning
* ⏰ Time management
* 🎓 Student planning
* ✈️ Trip preparation
* 📚 Study planning
* 🧾 Expense analysis
* 📊 Personal productivity

The architecture is designed so additional tools can be added without changing the overall agent workflow.

---

## 🔮 Future Enhancements

* 📊 Expense history and analytics
* 📝 Persistent user preferences
* 📅 Calendar integration
* ⏰ Reminder and notification tools
* 💳 Smarter financial planning
* 📈 Spending trend analysis
* 🌐 Deployment as a public web application
* 🧠 Advanced agent memory
* 🔌 Additional external APIs and tools
* 📱 Mobile-friendly interface

---

## 🔐 Security

LifeOps uses environment variables for API credentials.

Sensitive files such as:

```text
.env
venv/
__pycache__/
```

are excluded from version control using `.gitignore`.

**Never publish your API key in source code or GitHub.**

---

## 🌟 Why LifeOps?

Traditional applications usually follow:

```text
User → Function → Result
```

LifeOps follows an agentic workflow:

```text
User
  ↓
Understand Situation
  ↓
Determine Required Information
  ↓
Select Tools
  ↓
Execute Tools
  ↓
Combine Results
  ↓
Reason About Situation
  ↓
Provide Recommendation
```

This makes LifeOps more than a collection of utility functions.

It demonstrates how an **AI agent can combine language understanding, tool calling, computation and decision support** to solve practical problems.

---

## 👩‍💻 Author

### Poorani S

B.Tech Artificial Intelligence & Data Science

Interested in:

* Artificial Intelligence
* Generative AI
* Machine Learning
* Data Science
* AI Agents
* Software Development

---

## 📌 Project Status


**Status:** 🚀 Active Development

**Current Version:** v1.0

**Core Features:** ✅ Completed

**Multi-Tool Agent:** ✅ Implemented

**Gradio Interface:** ✅ Implemented

**GitHub Repository:** ✅ Available


**Status:** 🚀 Active Development

**Current Version:** v1.0

**Core Features:** ✅ Completed

**Multi-Tool Agent:** ✅ Implemented

**Gradio Interface:** ✅ Implemented

**GitHub Repository:** ✅ Available

