from finvizfinance.screener.overview import Overview

class FinivizData:

    def finiviz_screener(self):
        self.screener = Overview()
        self.filters_dict = {'Index': 'Any', "Current Volume": "Over 50K", "Gap": "Up 5%",
                        "Float": "Under 100M", "Market Cap.": "Any", "Price": "Over $1"}
        self.screener.set_filter(filters_dict=self.filters_dict)
        df_rth_screener = self.screener.screener_view(order="Change", ascend=False)
        '''
        new_column_float = []
        for ticker in df_rth["Ticker"]:
            stock = finvizfinance(ticker)
            stock_fundament = stock.ticker_fundament()
            shs_float = stock_fundament["Shs Float"]
            new_column_float.append(float(shs_float[0:-1]))
        '''
        return df_rth_screener

    def finiviz_tickers(self, df):
        return df["Ticker"]


class RetrievingFinivizData:

    def __init__(self):
        self.finiviz_data = FinivizData()

    def finiviz_stocks_screener(self):
        finiviz_stocks_dataframe = self.finiviz_data.finiviz_screener()
        return finiviz_stocks_dataframe

    def finiviz_tickers(self):
        finiviz_tickers = self.finiviz_data.finiviz_tickers(self.finiviz_data.finiviz_screener())
        return finiviz_tickers

