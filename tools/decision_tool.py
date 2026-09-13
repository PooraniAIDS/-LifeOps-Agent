def make_budget_decision(remaining_balance, event_days):
    """
    Analyze the user's remaining money and upcoming event timeframe.
    Returns a structured recommendation.
    """

    if remaining_balance < 0:
        status = "OVER_BUDGET"
        recommendation = (
            "Your listed expenses exceed your available money. "
            "Avoid additional non-essential spending and review your expenses."
        )

    elif remaining_balance < 500:
        status = "VERY_TIGHT"
        recommendation = (
            "Your remaining balance is very low. "
            "Keep the remaining money for essential expenses and avoid unnecessary spending."
        )

    elif remaining_balance < 1500:
        status = "LIMITED"
        recommendation = (
            "Your remaining balance is limited. "
            "Set a strict budget for the upcoming event and keep some money as a reserve."
        )

    elif event_days <= 3:
        status = "EVENT_SOON"
        recommendation = (
            "The event is very close. "
            "Finalize only essential event expenses and avoid last-minute unnecessary purchases."
        )

    else:
        status = "STABLE"
        recommendation = (
            "You have money remaining after the listed expenses. "
            "Set an event budget, keep a reserve for unexpected costs, and avoid unnecessary spending."
        )

    return {
        "status": status,
        "remaining_balance": remaining_balance,
        "days_until_event": event_days,
        "recommendation": recommendation
    }


if __name__ == "__main__":
    result = make_budget_decision(3500, 10)

    print("Status:", result["status"])
    print("Remaining Balance:", result["remaining_balance"])
    print("Days Until Event:", result["days_until_event"])
    print("Recommendation:", result["recommendation"])