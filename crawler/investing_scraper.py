import pandas as pd
import urllib.request
from configparser import ConfigParser

config = ConfigParser()
config.read('/Users/lauraschiavulli/Downloads/python/edgar/config/config.ini')


class InvestingData:

    def __init__(self):
        self.headers = {'User-Agent': config.get('INVESTING', 'USER_AGENT')}
        self.request = urllib.request.Request(config.get('INVESTING', 'URL'), None, self.headers)
        self.response = urllib.request.urlopen(self.request)
        self.data = self.response.read()

    def investing_screener(self):
        table = pd.read_html(self.data, match='Symbol')
        df_premarket_screener = table[0]
        return df_premarket_screener

    def investing_tickers(self, df):
        return df["Symbol"]


class RetrievingInvestingData:

    def __init__(self):
        self.investing_data = InvestingData()

    def investing_stocks_screener(self):
        investing_stocks_dataframe = self.investing_data.investing_screener()
        return investing_stocks_dataframe

    def investing_tickers(self):
        investing_tickers = self.investing_data.investing_tickers(self.investing_data.investing_screener())
        return investing_tickers
