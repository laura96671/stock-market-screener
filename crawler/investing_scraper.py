import pandas as pd
import urllib.request
import os

user_agent = os.getenv('USER_AGENT')
url = os.getenv('URL')


class InvestingData:

    def __init__(self):
        self.headers = {'User-Agent': user_agent}
        self.request = urllib.request.Request(url, None, self.headers)
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
