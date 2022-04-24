'''
HISTORIC DATABASE
'''

CREATE TABLE IF NOT EXISTS edgar_stock_screener (
    Ticker VARCHAR(10),
    Price FLOAT,
    Change_Pct FLOAT,
    Volume INT,
    Datetime TIMESTAMP,
    Provider VARCHAR(15)
);
