import os
import json

from dotenv import load_dotenv
from groq import Groq

from tools.time_tool import get_current_time
from tools.date_tool import calculate_date
from tools.expense_tool import calculate_expense
from tools.decision_tool import make_budget_decision


# ============================================================
# LOAD ENVIRONMENT
# ============================================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY not found. Please add it to your .env file."
    )

client = Groq(api_key=api_key)


# ============================================================
# TOOLS AVAILABLE TO THE AGENT
# ============================================================

tools = [

    # --------------------------------------------------------
    # TIME TOOL
    # --------------------------------------------------------

    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current local time.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },

    # --------------------------------------------------------
    # DATE TOOL
    # --------------------------------------------------------

    {
        "type": "function",
        "function": {
            "name": "calculate_date",
            "description": (
                "Calculate a date a certain number of days "
                "before or after today."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "days": {
                        "type": "integer",
                        "description": (
                            "Number of days. "
                            "Positive for future, "
                            "negative for past."
                        )
                    }
                },
                "required": ["days"]
            }
        }
    },

    # --------------------------------------------------------
    # EXPENSE TOOL
    # --------------------------------------------------------

    {
        "type": "function",
        "function": {
            "name": "calculate_expense",
            "description": (
                "Calculate total expenses "
                "and remaining balance."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "income": {
                        "type": "number",
                        "description": "Total available money."
                    },
                    "expenses": {
                        "type": "array",
                        "items": {
                            "type": "number"
                        },
                        "description": (
                            "List of individual expense amounts."
                        )
                    }
                },
                "required": [
                    "income",
                    "expenses"
                ]
            }
        }
    },

    # --------------------------------------------------------
    # DECISION TOOL
    # --------------------------------------------------------

    {
        "type": "function",
        "function": {
            "name": "make_budget_decision",
            "description": (
                "Analyze the remaining money and "
                "upcoming event timeframe to provide "
                "a practical budget recommendation."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "remaining_balance": {
                        "type": "number",
                        "description": (
                            "Money remaining after "
                            "listed expenses."
                        )
                    },
                    "event_days": {
                        "type": "integer",
                        "description": (
                            "Number of days until "
                            "the upcoming event."
                        )
                    }
                },
                "required": [
                    "remaining_balance",
                    "event_days"
                ]
            }
        }
    }
]


# ============================================================
# TOOL EXECUTION
# ============================================================

def run_tool(name, arguments):

    try:

        # ----------------------------------------------------
        # TIME
        # ----------------------------------------------------

        if name == "get_current_time":

            return get_current_time()

        # ----------------------------------------------------
        # DATE
        # ----------------------------------------------------

        elif name == "calculate_date":

            days = arguments.get("days")

            if days is None:
                return {
                    "error": "The number of days is required."
                }

            return calculate_date(days)

        # ----------------------------------------------------
        # EXPENSE
        # ----------------------------------------------------

        elif name == "calculate_expense":

            income = arguments.get("income")
            expenses = arguments.get("expenses")

            if income is None or expenses is None:
                return {
                    "error": (
                        "Income and expenses "
                        "are required."
                    )
                }

            if not isinstance(expenses, list):
                return {
                    "error": (
                        "Expenses must be provided "
                        "as a list of numbers."
                    )
                }

            return calculate_expense(
                income,
                expenses
            )

        # ----------------------------------------------------
        # DECISION
        # ----------------------------------------------------

        elif name == "make_budget_decision":

            remaining_balance = arguments.get(
                "remaining_balance"
            )

            event_days = arguments.get(
                "event_days"
            )

            if (
                remaining_balance is None
                or event_days is None
            ):
                return {
                    "error": (
                        "Remaining balance and "
                        "event days are required."
                    )
                }

            return make_budget_decision(
                remaining_balance,
                event_days
            )

        # ----------------------------------------------------
        # UNKNOWN TOOL
        # ----------------------------------------------------

        return {
            "error": f"Unknown tool: {name}"
        }

    except Exception as error:

        return {
            "error": (
                f"Tool execution failed: {str(error)}"
            )
        }


# ============================================================
# LIFEOPS AGENT
# ============================================================

def run_agent(user_message):

    if not user_message or not user_message.strip():

        return (
            "Please describe your situation "
            "so I can help you."
        )

    messages = [

        # ----------------------------------------------------
        # SYSTEM PROMPT
        # ----------------------------------------------------

        {
            "role": "system",

            "content": """

You are LifeOps Agent, an intelligent personal
decision-support assistant.

Your purpose is to help users understand everyday
situations and make practical decisions.

You are not simply a calculator.

You should:

1. Understand the user's situation.

2. Identify what information is required.

3. Decide which tools are useful.

4. Use the appropriate tools autonomously.

5. Use multiple tools when necessary.

6. Chain tool results together when one result
   is needed as input for another tool.

7. Analyze the collected information.

8. Provide a clear and practical recommendation.

Available tools:

TIME TOOL
- get_current_time
- Returns the current local time.

DATE TOOL
- calculate_date
- Calculates a date before or after today.

EXPENSE TOOL
- calculate_expense
- Calculates total expenses and remaining balance.

DECISION TOOL
- make_budget_decision
- Analyzes remaining money and event timeframe
  and provides a practical recommendation.

IMPORTANT RULES:

- Choose tools autonomously.
- Do not use tools unnecessarily.
- Use multiple tools when the situation requires them.
- Never invent tool results.
- Always use actual tool results for calculations.
- If a tool result is required for another tool,
  use the previous result as the next tool's input.
- For budget recommendations, use the decision tool.
- Clearly explain important calculations.
- Do not expose internal tool calls to the user.
- Do not describe the technical tool execution process
  unless the user specifically asks about it.
- Keep the final answer concise, useful and practical.
- Focus on helping the user make a decision.

Example of multi-tool reasoning:

If the user provides money, expenses and an
upcoming event:

1. Calculate the remaining balance.
2. Calculate the event date.
3. Get the current time if requested.
4. Pass the remaining balance and event timeframe
   to the decision tool.
5. Combine all results into one useful response.

You are a decision-support agent, not just a calculator.

"""
        },

        # ----------------------------------------------------
        # USER MESSAGE
        # ----------------------------------------------------

        {
            "role": "user",
            "content": user_message
        }
    ]


    # ========================================================
    # AGENT LOOP
    # ========================================================

    while True:

        try:

            response = client.chat.completions.create(

                model="openai/gpt-oss-120b",

                messages=messages,

                tools=tools,

                tool_choice="auto"
            )

        except Exception as error:

            return (
                "⚠️ I couldn't connect to the AI service "
                "right now.\n\n"
                f"Error: {str(error)}"
            )


        assistant_message = response.choices[0].message


        # ====================================================
        # NO MORE TOOLS REQUIRED
        # ====================================================

        if not assistant_message.tool_calls:

            return (
                assistant_message.content
                or "I couldn't generate a response."
            )


        # ====================================================
        # ADD ASSISTANT TOOL REQUEST
        # ====================================================

        messages.append({

            "role": "assistant",

            "content": assistant_message.content,

            "tool_calls": [

                {
                    "id": tool_call.id,

                    "type": "function",

                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments
                    }
                }

                for tool_call in assistant_message.tool_calls
            ]
        })


        # ====================================================
        # EXECUTE TOOLS
        # ====================================================

        for tool_call in assistant_message.tool_calls:

            tool_name = tool_call.function.name


            # ------------------------------------------------
            # PARSE TOOL ARGUMENTS SAFELY
            # ------------------------------------------------

            try:

                arguments = json.loads(
                    tool_call.function.arguments
                )

            except json.JSONDecodeError:

                result = {
                    "error": (
                        "The AI generated invalid "
                        "tool arguments."
                    )
                }

                messages.append({

                    "role": "tool",

                    "tool_call_id": tool_call.id,

                    "content": json.dumps(result)
                })

                continue


            # ------------------------------------------------
            # RUN TOOL
            # ------------------------------------------------

            result = run_tool(
                tool_name,
                arguments
            )


            # ------------------------------------------------
            # SEND TOOL RESULT BACK TO AI
            # ------------------------------------------------

            messages.append({

                "role": "tool",

                "tool_call_id": tool_call.id,

                "content": json.dumps(result)
            })


# ============================================================
# TERMINAL TEST MODE
# ============================================================

if __name__ == "__main__":

    print("=" * 55)
    print("🧠 LifeOps Agent")
    print("Personal Decision Support Assistant")
    print("=" * 55)

    user_message = input("\nYou: ")

    result = run_agent(user_message)

    print("\n🤖 LifeOps Agent:")
    print(result)