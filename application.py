#qui andra' importata funzione per definire se siamo in rth o premarket
from screener.screener import ScreenerExecution
from news.news import SearchingNews
from util.utility import time_of_day
from database.database import Database
import warnings


warnings.simplefilter(action='ignore', category=FutureWarning)


"""
Entry point of the edgar application.

:return:
"""
screener_execution = ScreenerExecution()
news_execution = SearchingNews()
database = Database()


#while True:
if time_of_day() == "PREMARKET":
    print("Retrieving top premarket movers...")
    print(screener_execution.premarket_screener_execution())
    database.premarket_db_screener()

    print("===")

    print("Retrieving latest premarket news...")
    print(news_execution.premarket_news_crawler())
    database.premarket_news_screener()

    #sleep for x secs


elif time_of_day() == "REGULAR TRADING HOURS":
    print("Retrieving top movers...")
    print(screener_execution.rth_screener_execution())
    database.rth_db_screener()

    print("===")

    print("Retrieving latest news...")
    print(news_execution.rth_news_crawler())
    database.rth_news_screener()

    # sleep for x secs

#else:
    #sleep
