import requests as r
import pandas as pd 

iex_base_url = "https://api.iextrading.com/1.0/"

def list_symbols():
	req = r.get(iex_base_url+"ref-data/symbols") 
	symbols = req.json()
	symbol_list = [{'data':stock['symbol'], 'value':stock['name']} for stock in symbols]
	return symbol_list
