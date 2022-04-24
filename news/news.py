from crawler.finiviz_api import RetrievingFinivizData
from crawler.investing_scraper import RetrievingInvestingData
from finvizfinance.quote import finvizfinance
import pandas as pd
from tabulate import tabulate
from datetime import date


class News:

    def premarket_news(self, tickers):
        for ticker in tickers:
            self.stock = finvizfinance(ticker)
            df_prem_news = self.stock.ticker_news()
            df_prem_news["Stock"] = ticker
            self.today = date.today()
            df_prem_news["Provider"] = "PREMARKET"
            df_prem_news = df_prem_news[df_prem_news.Date >= self.today]
            df_prem_news = df_prem_news[["Stock", "Date", "Title", "Link", "Provider"]]
            df_prem_news.dropna(inplace=True)

            self.value = 30  # increment value for text wrap
            df_prem_news["Title"] = df_prem_news["Title"].apply(
                lambda x: '\n'.join([x[i:i + self.value] for i in range(0, len(x), self.value)]))
            df_prem_news["Link"] = df_prem_news["Link"].apply(
                lambda x: '\n'.join([x[i:i + self.value] for i in range(0, len(x), self.value)]))

            if df_prem_news.shape[0] > 0:
                return df_prem_news
                #print(tabulate(df_prem_news, headers='keys', tablefmt='psql'))

    def rth_news(self, tickers):
        for ticker in tickers:
            self.stock = finvizfinance(ticker)
            df_rth_news = self.stock.ticker_news()
            df_rth_news["Stock"] = ticker
            self.today = date.today()
            df_rth_news["Provider"] = "RTH"
            df_rth_news = df_rth_news[df_rth_news.Date >= self.today]
            df_rth_news = df_rth_news[["Stock", "Date", "Title", "Link", "Provider"]]

            df_rth_news.dropna(inplace=True)

            self.value = 30  # increment value for text wrap
            df_rth_news["Title"] = df_rth_news["Title"].apply(
                lambda x: '\n'.join([x[i:i + self.value] for i in range(0, len(x), self.value)]))
            df_rth_news["Link"] = df_rth_news["Link"].apply(
                lambda x: '\n'.join([x[i:i + self.value] for i in range(0, len(x), self.value)]))

            if df_rth_news.shape[0] > 0:
                return df_rth_news
                #print(tabulate(df_rth_news, headers='keys', tablefmt='psql'))


class SearchingNews:

    def __init__(self):
        self.news = News()
        self.rth = RetrievingFinivizData()
        self.prem = RetrievingInvestingData()

    def premarket_news_crawler(self):
        prem_news = self.news.premarket_news(self.prem.investing_tickers())
        return prem_news

    def rth_news_crawler(self):
        rth_news = self.news.rth_news(self.rth.finiviz_tickers())
        return rth_news
