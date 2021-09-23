import pandas as pd
import yfinance as yf
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

#connection
scope =["https://spreadsheets.google.com/feeds",
        'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
   "credentials.json",
    scope
)
client = gspread.authorize(credentials)

#dataframes
portfolioSheet = client.open("yFinance-sheets").worksheet("portfolio")
tickers = pd.DataFrame(portfolioSheet.col_values(2)).iloc[3:]

#yFinance_iteration
for index, row in tickers.iterrows():
    ticker = yf.Ticker(row.to_string())
    financials = ticker.financials
    print(ticker)

