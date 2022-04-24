from sqlalchemy import create_engine
from configparser import ConfigParser
from screener.screener import ScreenerExecution
from news.news import SearchingNews
import warnings


warnings.simplefilter(action='ignore', category=FutureWarning)

config = ConfigParser()
config.read('/Users/lauraschiavulli/Downloads/python/edgar/config/config.ini')

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host = 'localhost',
                                                                        db = 'Edgar',
                                                                        user = config.get('DATABASE', 'USER'),
                                                                        pw = config.get('DATABASE', 'PASSWORD')))

'''
REAL TIME DATABASE
'''

class Database:

    def __init__(self):
        self.screener_df = ScreenerExecution()
        self.news_df = SearchingNews()

    def premarket_db_screener(self):
        real_time_premarket_db = self.screener_df.premarket_screener_execution().\
                        to_sql('real_time_screener', engine, if_exists='replace', index=False)

    def premarket_news_screener(self):
        if self.news_df.premarket_news_crawler() is not None:
            real_time_premarket_news_db = self.news_df.premarket_news_crawler().\
                            to_sql('real_time_news', engine, if_exists='replace', index=False)
        else:
            print("Found 0 news feeds")

    def rth_db_screener(self):
        real_time_rth_db = self.screener_df.rth_screener_execution().\
                        to_sql('real_time_screener', engine, if_exists='replace', index=False)

    def rth_news_screener(self):
        if self.news_df.rth_news_crawler() is not None:
            real_time_rth_news_db = self.news_df.rth_news_crawler().\
                            to_sql('real_time_news', engine, if_exists='replace', index=False)
        else:
            print("Found 0 news feeds")
