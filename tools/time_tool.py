from datetime import datetime


def get_current_time():
    """Returns the current local time."""
    current_time = datetime.now()
    return current_time.strftime("%I:%M:%S %p")


if __name__ == "__main__":
    print("Current Time:", get_current_time())