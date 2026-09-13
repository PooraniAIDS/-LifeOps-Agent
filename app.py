import gradio as gr
from agent import run_agent


# ============================================================
# CHAT FUNCTION
# ============================================================

def chat_with_agent(message, history):

    if not message.strip():
        return "⚠️ Please describe your situation."

    try:
        return run_agent(message)

    except Exception as error:
        return (
            "⚠️ Something went wrong while processing "
            "your request.\n\n"
            f"Error: {str(error)}"
        )


# ============================================================
# CUSTOM CSS
# ============================================================

css = """
body {
    background: #f5f7fb;
}

.gradio-container {
    max-width: 1100px !important;
    margin: auto;
}

#title {
    text-align: center;
    margin-bottom: 5px;
}

#subtitle {
    text-align: center;
    color: #666;
    margin-bottom: 25px;
}

.tool-card {
    border-radius: 12px;
    padding: 15px;
    background: white;
    border: 1px solid #e5e7eb;
}
"""


# ============================================================
# LIFEOPS WEB APP
# ============================================================

with gr.Blocks(
    title="LifeOps Agent",
    css=css
) as demo:

    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    gr.Markdown(
        """
        # 🧠 LifeOps Agent
        """,
        elem_id="title"
    )

    gr.Markdown(
        """
        **AI-powered personal decision assistant**

        Describe your everyday situation. LifeOps analyzes it,
        selects the appropriate tools, and gives you a
        practical recommendation.
        """,
        elem_id="subtitle"
    )


    # --------------------------------------------------------
    # TOOL CARDS
    # --------------------------------------------------------

    with gr.Row():

        with gr.Column(elem_classes="tool-card"):
            gr.Markdown(
                """
                ### 🕐 Time Tool

                Get the current local time.
                """
            )

        with gr.Column(elem_classes="tool-card"):
            gr.Markdown(
                """
                ### 📅 Date Tool

                Calculate future or past dates.
                """
            )

        with gr.Column(elem_classes="tool-card"):
            gr.Markdown(
                """
                ### 💰 Expense Tool

                Calculate expenses and remaining balance.
                """
            )

        with gr.Column(elem_classes="tool-card"):
            gr.Markdown(
                """
                ### 🧠 Decision Tool

                Generate practical recommendations.
                """
            )


    gr.Markdown("---")


    # --------------------------------------------------------
    # CHAT INTERFACE
    # --------------------------------------------------------

    chatbot = gr.ChatInterface(

    fn=chat_with_agent,

    title="💬 Talk to LifeOps",

    description=(
        "Describe your everyday situation. "
        "LifeOps will analyze it, use the appropriate "
        "tools, and provide a practical recommendation."
    ),

    examples=[
        "What time is it now?",
        "What date will it be 15 days from today?",
        (
            "I have ₹5000 and my expenses are "
            "₹500, ₹300 and ₹700. "
            "How much money will I have left?"
        ),
        (
            "I have ₹5000 and my expenses are "
            "₹500, ₹300 and ₹700. "
            "I have an important event 10 days from now. "
            "Tell me the event date, remaining money, "
            "current time and give me a practical "
            "recommendation."
        )
    ],

    textbox=gr.Textbox(
        placeholder="💭 Describe your situation...",
        lines=3,
        submit_btn="🚀 Send"
    )
)


    # --------------------------------------------------------
    # CAPABILITIES
    # --------------------------------------------------------

    gr.Markdown(
        """
        ---

        ### 🔧 Available Agent Capabilities

        `Time` • `Date Calculation` • `Expense Analysis` • `Budget Decision`

        **LifeOps doesn't just answer — it analyzes, uses tools,
        and makes practical decisions.**
        """
    )


# ============================================================
# LAUNCH
# ============================================================

if __name__ == "__main__":
    demo.launch()