'''
HISTORIC DATABASES
'''

# Stock Screener

CREATE TABLE IF NOT EXISTS edgar_stock_screener (
    Ticker VARCHAR(10),
    Price FLOAT,
    Change_Pct FLOAT,
    Volume INT,
    Datetime TIMESTAMP,
    Provider VARCHAR(15)
);


# News Screener

CREATE TABLE IF NOT EXISTS edgar_news_screener (
    Stock VARCHAR(10),
    Datetime TIMESTAMP,
    Title TEXT,
    Link TEXT
);


'''
EVENTS
'''

# Stock Screener Event

delimiter |

CREATE EVENT IF NOT EXISTS stock_screener_store
    ON SCHEDULE
        EVERY 1 DAY
            STARTS
            END |

delimiter ;

