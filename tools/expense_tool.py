def calculate_expense(income, expenses):
    """
    Calculate total expenses and remaining balance.

    income: total available money
    expenses: list of expense amounts
    """

    total_expense = sum(expenses)
    remaining = income - total_expense

    return {
        "income": income,
        "total_expense": total_expense,
        "remaining_balance": remaining
    }


if __name__ == "__main__":
    income = 5000
    expenses = [500, 300, 250, 100]

    result = calculate_expense(income, expenses)

    print("Income:", result["income"])
    print("Total Expenses:", result["total_expense"])
    print("Remaining Balance:", result["remaining_balance"])