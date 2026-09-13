import gradio as gr
from agent import run_agent


# ============================================================
# TOOL INFORMATION
# ============================================================

TOOL_INFO = {
    "get_current_time": ("🕐", "Current Time"),
    "calculate_date": ("📅", "Date Calculation"),
    "calculate_expense": ("💰", "Expense Analysis"),
    "make_budget_decision": ("🧠", "Budget Decision"),
}


# ============================================================
# CHAT FUNCTION
# ============================================================

def chat_with_agent(message, history):

    if not message or not message.strip():
        return (
            "⚠️ Please describe your situation.",
            "### 🛠️ Agent Activity\n\nNo tools used."
        )

    try:

        result = run_agent(message)

        response = result["response"]
        tools_used = result["tools_used"]

        if tools_used:

            activity = "### 🛠️ Agent Activity\n\n"

            for tool in tools_used:

                icon, name = TOOL_INFO.get(
                    tool,
                    ("🔧", tool)
                )

                activity += (
                    f"✅ {icon} **{name}**\n"
                )

            activity += (
                "\n---\n"
                "🧠 *Tools were selected autonomously "
                "based on your situation.*"
            )

        else:

            activity = (
                "### 🛠️ Agent Activity\n\n"
                "ℹ️ No external tools were required."
            )

        return response, activity

    except Exception as error:

        return (
            "⚠️ Something went wrong while processing your request.",
            f"### ❌ Error\n\n`{str(error)}`"
        )


# ============================================================
# CUSTOM CSS
# ============================================================

css = """

body {
    background: #f4f6fb;
}

.gradio-container {
    max-width: 1150px !important;
    margin: auto !important;
}


/* HEADER */

#title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-top: 20px;
    margin-bottom: 5px;
}

#subtitle {
    text-align: center;
    font-size: 17px;
    color: #667085;
    margin-bottom: 30px;
}


/* TOOL CARDS */

.tool-card {
    border-radius: 16px;
    padding: 18px;
    background: white;
    border: 1px solid #e4e7ec;
    min-height: 125px;
}


/* ACTIVITY */

.activity-panel {
    border-radius: 16px;
    padding: 18px;
    background: white;
    border: 1px solid #e4e7ec;
}


/* FOOTER */

.footer {
    text-align: center;
    color: #667085;
    font-size: 14px;
    margin-top: 20px;
}

"""


# ============================================================
# LIFEOPS WEB APP
# ============================================================

with gr.Blocks(
    title="LifeOps Agent",
    css=css
) as demo:


    # ========================================================
    # HEADER
    # ========================================================

    gr.Markdown(
        """
        # 🧠 LifeOps Agent
        """,
        elem_id="title"
    )

    gr.Markdown(
        """
        ### AI-Powered Personal Decision-Support Assistant

        **Describe a situation → Analyze → Decide → Recommend**
        """,
        elem_id="subtitle"
    )


    # ========================================================
    # TOOL CARDS
    # ========================================================

    with gr.Row():

        with gr.Column(
            elem_classes="tool-card"
        ):

            gr.Markdown(
                """
                ## 🕐 Current Time

                Get the current local time.
                """
            )


        with gr.Column(
            elem_classes="tool-card"
        ):

            gr.Markdown(
                """
                ## 📅 Date Calculator

                Calculate future or past dates.
                """
            )


        with gr.Column(
            elem_classes="tool-card"
        ):

            gr.Markdown(
                """
                ## 💰 Expense Analysis

                Calculate expenses and remaining balance.
                """
            )


        with gr.Column(
            elem_classes="tool-card"
        ):

            gr.Markdown(
                """
                ## 🧠 Budget Decision

                Generate practical recommendations.
                """
            )


    gr.Markdown("---")


    # ========================================================
    # CHAT + ACTIVITY
    # ========================================================

    with gr.Row():


        # ----------------------------------------------------
        # CHAT AREA
        # ----------------------------------------------------

        with gr.Column(scale=3):

            gr.Markdown(
                """
                ## 💬 Talk to LifeOps

                Tell the agent what you're dealing with.
                """
            )

            chatbot = gr.Chatbot(
                height=500,
                label="LifeOps Conversation"
            )

            with gr.Row():

                message_box = gr.Textbox(
                    placeholder=(
                        "💭 Describe your situation..."
                    ),
                    lines=3,
                    scale=5,
                    show_label=False
                )

                send_button = gr.Button(
                    "🚀 Send",
                    variant="primary",
                    scale=1
                )


            clear_button = gr.Button(
                "🗑️ Clear Conversation"
            )


        # ----------------------------------------------------
        # AGENT ACTIVITY
        # ----------------------------------------------------

        with gr.Column(
            scale=1,
            elem_classes="activity-panel"
        ):

            activity_output = gr.Markdown(
                """
                ### 🛠️ Agent Activity

                Tools selected by LifeOps will appear here.

                ---

                **Agent Workflow**

                🧠 Understand

                ↓

                🔍 Analyze

                ↓

                🛠️ Select Tools

                ↓

                🔗 Combine Results

                ↓

                💡 Recommend
                """
            )


    # ========================================================
    # SEND FUNCTION
    # ========================================================

    def send_message(message, history):

        if not message or not message.strip():

            return (
                history,
                "",
                "### 🛠️ Agent Activity\n\n"
                "⚠️ Please enter a situation."
            )

        try:

            result = run_agent(message)

            response = result["response"]
            tools_used = result["tools_used"]

            # Add user message
            history.append(
                {
                    "role": "user",
                    "content": message
                }
            )

            # Add agent response
            history.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )


            # Build activity
            if tools_used:

                activity = (
                    "### 🛠️ Agent Activity\n\n"
                )

                for tool in tools_used:

                    icon, name = TOOL_INFO.get(
                        tool,
                        ("🔧", tool)
                    )

                    activity += (
                        f"✅ {icon} **{name}**\n"
                    )

                activity += (
                    "\n---\n"
                    "🧠 *LifeOps selected these tools "
                    "autonomously.*"
                )

            else:

                activity = (
                    "### 🛠️ Agent Activity\n\n"
                    "ℹ️ No external tools were required."
                )


            return history, "", activity


        except Exception as error:

            history.append(
                {
                    "role": "user",
                    "content": message
                }
            )

            history.append(
                {
                    "role": "assistant",
                    "content": (
                        "⚠️ Something went wrong.\n\n"
                        f"`{str(error)}`"
                    )
                }
            )

            return (
                history,
                "",
                "### ❌ Error\n\n"
                "Something went wrong while processing your request."
            )


    # ========================================================
    # BUTTON CONNECTIONS
    # ========================================================

    send_button.click(
        send_message,
        inputs=[
            message_box,
            chatbot
        ],
        outputs=[
            chatbot,
            message_box,
            activity_output
        ]
    )


    message_box.submit(
        send_message,
        inputs=[
            message_box,
            chatbot
        ],
        outputs=[
            chatbot,
            message_box,
            activity_output
        ]
    )


    # ========================================================
    # CLEAR BUTTON
    # ========================================================

    def clear_chat():

        return [], "", (
            "### 🛠️ Agent Activity\n\n"
            "Conversation cleared.\n\n"
            "Ready for a new situation."
        )


    clear_button.click(
        clear_chat,
        outputs=[
            chatbot,
            message_box,
            activity_output
        ]
    )


    # ========================================================
    # EXAMPLES
    # ========================================================

    gr.Markdown("---")

    gr.Markdown(
        """
        ## 💡 Try These Examples
        """
    )

    gr.Examples(
        examples=[
            ["What time is it now?"],

            ["What date will it be 15 days from today?"],

            [
                "I have ₹5000 and my expenses are "
                "₹500, ₹300 and ₹700. "
                "How much money will I have left?"
            ],

            [
                "I have ₹5000 and my expenses are "
                "₹500, ₹300 and ₹700. "
                "I have an important event 10 days "
                "from now. Tell me the event date, "
                "remaining money, current time and "
                "give me a practical recommendation."
            ]
        ],
        inputs=message_box
    )


    # ========================================================
    # HOW IT WORKS
    # ========================================================

    gr.Markdown("---")

    gr.Markdown(
        """
        ## ⚡ How LifeOps Works

        | Stage | What happens |
        |---|---|
        | 🧠 **Understand** | Understand the user's situation |
        | 🔍 **Analyze** | Identify required information |
        | 🛠️ **Select Tools** | Choose useful tools automatically |
        | 🔗 **Combine** | Chain results when necessary |
        | 💡 **Recommend** | Give a practical recommendation |

        ### The key idea

        **LifeOps doesn't simply execute commands.**

        The AI agent decides **which tools are useful,
        when they are needed, and how their results
        should be combined.**
        """
    )


    # ========================================================
    # FOOTER
    # ========================================================

    gr.Markdown(
        """
        ---

        <div class="footer">

        🧠 <b>LifeOps Agent</b> • AI Decision Support System

        Built with Python • Groq • GPT-OSS 120B • Gradio

        </div>
        """
    )


# ============================================================
# LAUNCH
# ============================================================

if __name__ == "__main__":
    demo.launch()