from datetime import datetime, timedelta


def calculate_date(days):
    """Calculate a future or past date from today."""
    
    today = datetime.now().date()
    result_date = today + timedelta(days=days)

    return result_date.strftime("%d %B %Y")


if __name__ == "__main__":
    print("Today:", datetime.now().strftime("%d %B %Y"))
    print("After 7 days:", calculate_date(7))
    print("Before 7 days:", calculate_date(-7))