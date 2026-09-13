````markdown
# 🧠 LifeOps Agent

### AI-Powered Personal Decision Support Assistant

LifeOps Agent is an AI-powered personal decision-support assistant that helps users analyze everyday situations and make practical decisions.

Instead of simply answering questions, the agent understands the user's situation, autonomously selects the appropriate tools, combines the results, and generates a useful recommendation.

---

## 🚀 Key Features

- 🤖 AI-powered decision support
- 🕐 Current time calculation
- 📅 Future and past date calculation
- 💰 Expense and balance calculation
- 🧠 Budget-based recommendations
- 🔄 Autonomous tool selection
- 🔗 Multi-tool execution and chaining
- 💬 Interactive Gradio web interface

---

## 🏗️ Architecture

```text
                    USER
                      ↓
                LIFEOPS AGENT
                      ↓
                     LLM
                      ↓
                TOOL SELECTION
                      ↓
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
     TIME TOOL     DATE TOOL    EXPENSE TOOL
        ↓             ↓             ↓
        └─────────────┼─────────────┘
                      ↓
                DECISION TOOL
                      ↓
               AGENT REASONING
                      ↓
          RECOMMENDATION & ACTION
````

---

## 🛠️ Available Tools

### 🕐 Time Tool

Returns the current local time.

**Function:**

```text
get_current_time()
```

---

### 📅 Date Tool

Calculates a future or past date based on the number of days.

**Function:**

```text
calculate_date(days)
```

---

### 💰 Expense Tool

Calculates the total expenses and remaining balance.

**Function:**

```text
calculate_expense(income, expenses)
```

---

### 🧠 Decision Tool

Analyzes the remaining balance and upcoming event timeframe to generate a practical recommendation.

**Function:**

```text
make_budget_decision(remaining_balance, event_days)
```

---

## 💡 Example Use Case

### User Input

```text
I have ₹5000 and my expenses are ₹500, ₹300 and ₹700.
I have an important event 10 days from now.
Tell me the event date, how much money I will have left,
and give me a practical recommendation.
```

### Agent Process

```text
User Situation
      ↓
Calculate Expenses
      ↓
Calculate Event Date
      ↓
Analyze Remaining Balance
      ↓
Generate Recommendation
```

The agent autonomously selects the required tools, executes them, combines their results, and provides a practical response.

---

## 🧰 Tech Stack

* **Python** – Core programming language
* **Groq API** – LLM API
* **GPT-OSS 120B** – Language model
* **Gradio** – Web interface
* **python-dotenv** – Environment variable management
* **Custom Tool Calling** – Agent tool execution and orchestration

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
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd LifeOps-Agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

For Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Configuration

Create a `.env` file in the project root.

Add your Groq API key:

```text
GROQ_API_KEY=your_api_key_here
```

**Important:** Never upload your `.env` file or API key to GitHub.

---

## ▶️ Running the Application

Start the Gradio application using:

```bash
python app.py
```

After starting the application, a local URL will appear in the terminal.

Open the URL in your browser to use LifeOps Agent.

---

## 🎯 How It Works

LifeOps Agent follows a simple agentic workflow:

### 1. Understand

The agent understands the user's situation and identifies what information is required.

### 2. Select

The LLM autonomously selects the tools required to solve the user's request.

### 3. Execute

The selected tools are executed using the required inputs.

### 4. Chain

If the result of one tool is required by another tool, the agent passes the result forward.

### 5. Analyze

The agent combines the collected information and analyzes the situation.

### 6. Recommend

Finally, LifeOps provides a clear and practical recommendation.

---

## 🔄 Multi-Tool Example

For a request involving money, expenses, an upcoming event, and current time, the agent can use multiple tools:

```text
User
 ↓
LifeOps Agent
 ↓
 ├── Time Tool
 ├── Date Tool
 ├── Expense Tool
 └── Decision Tool
 ↓
Combined Results
 ↓
AI Reasoning
 ↓
Practical Recommendation
```

This demonstrates autonomous multi-tool execution instead of a simple single-function chatbot.

---

## 🌟 Why LifeOps Agent?

Traditional chatbots mainly provide answers.

LifeOps Agent focuses on **decision support**.

```text
Traditional Chatbot
        ↓
     Question
        ↓
      Answer


LifeOps Agent
        ↓
     Situation
        ↓
     Analyze
        ↓
   Select Tools
        ↓
  Execute Tools
        ↓
 Combine Results
        ↓
     Reason
        ↓
   Recommendation
```

The goal is to demonstrate how an AI agent can use external tools and reasoning to solve practical, real-world problems.

---

## 🔮 Future Improvements

Possible future enhancements include:

* 📊 Personal spending analytics
* 💰 Savings goal tracking
* 📅 Calendar integration
* 🔔 Smart reminders
* 🧾 Receipt analysis
* 🎯 Personalized financial goals
* 💬 Conversation memory
* 📱 Mobile-friendly interface
* 📈 Spending trend visualization
* 🤝 Integration with additional AI tools

---

## 🧪 Sample Queries

Try these queries with LifeOps Agent:

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
Tell me the event date, remaining money and give me
a practical recommendation.
```

---

## 🔐 Security

The project uses environment variables to store the Groq API key.

The `.env` file is excluded from version control using `.gitignore`.

Never expose your API key publicly.

---

## 👩‍💻 Author

**Poorani S**

B.Tech Artificial Intelligence & Data Science

---

## ⭐ Project Highlights

* AI Agent
* Function Calling
* Autonomous Tool Selection
* Multi-Tool Execution
* Tool Chaining
* Decision Support
* LLM Reasoning
* Gradio Interface

---

⭐ **If you find this project useful, consider giving the repository a star!**

```
```
