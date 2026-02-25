import datetime


def get_current_time() -> dict:
    """ 
    This is a tool that returns the current time in the format YYYY-MM-DD HH:MM:SS.
    This tool can be used by the agent if the user request the current time.
    """

    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }