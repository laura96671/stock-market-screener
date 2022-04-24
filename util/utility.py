from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S")

def time_of_day():
    if current_time <= '15:29:00':
        market_time = "PREMARKET"
    elif current_time >= '15:30:00':
        market_time = "REGULAR TRADING HOURS"

    return market_time
