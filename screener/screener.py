from crawler.investing_scraper import RetrievingInvestingData
from crawler.finiviz_api import RetrievingFinivizData
from datetime import date
from datetime import datetime as dt
from pytz import timezone
import pandas as pd


class Screener:

    def premarket_screener(self, df_prem_screen):
        df_prem_screen["Chg. %"] = df_prem_screen["Chg. %"].replace({"%": ""}, regex=True).astype(float)
        df_prem_screen["Vol."] = df_prem_screen["Vol."].replace({"K": "*1e3", "M": "*1e6", "B": "*1e9"}, regex=True).map(pd.eval).astype(int)

        self.today = date.today()
        today = self.today.strftime('%Y-%m-%d')
        df_prem_screen["Time"] = today + " " + df_prem_screen["Time"]
        df_prem_screen["Time"] = pd.to_datetime(df_prem_screen["Time"], format='%Y-%m-%d %H:%M:%S')
        df_prem_screen["Provider"] = "PREMARKET"

        df_prem_screen = df_prem_screen.loc[:, ~df_prem_screen.columns.str.contains('^Unnamed')]
        df_prem_screen = df_prem_screen.sort_values('Chg. %', ascending=False, ignore_index=True)

        df_prem_screen.rename(columns={'Symbol': 'Ticker',
                                       'Last': 'Price',
                                       'Chg. %': 'Change_pct',
                                       'Vol.': 'Volume',
                                       'Time': 'Datetime'}, inplace=True)
        return df_prem_screen[["Ticker", "Price", "Change_pct", "Volume", "Datetime", "Provider"]]

    def rth_screener(self, df_rth):
        self.today = date.today()
        today = self.today.strftime('%Y-%m-%d')
        self.eastern = timezone('US/Eastern')
        current_time = dt.now(self.eastern).strftime("%H:%M:%S")
        current_datetime = today + " " + current_time
        df_rth["Datetime"] = pd.to_datetime(current_datetime, format='%Y-%m-%d %H:%M:%S')
        df_rth["Provider"] = "RTH"

        df_rth.rename(columns={'Change': 'Change_pct'}, inplace=True)
        df_rth = df_rth[["Ticker", "Price", "Change_pct", "Volume", "Datetime", "Provider"]]
        return df_rth


class ScreenerExecution:

    def __init__(self):
        self.whole_screener = Screener()
        self.retrieving_investing_data = RetrievingInvestingData()
        self.retrieving_finiviz_data = RetrievingFinivizData()

    def premarket_screener_execution(self):
        premarket_screener = self.whole_screener.premarket_screener(self.retrieving_investing_data.investing_stocks_screener())
        return premarket_screener

    def rth_screener_execution(self):
        rth_screener = self.whole_screener.rth_screener(self.retrieving_finiviz_data.finiviz_stocks_screener())
        return rth_screener

