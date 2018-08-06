import requests as r
import pandas as pd 

iex_base_url = "https://api.iextrading.com/1.0/"

def list_symbols():
	req = r.get(iex_base_url+"ref-data/symbols") 
	symbols = req.json()
	symbol_list = [{'data':stock['symbol'], 'value':stock['name']} for stock in symbols]
	return symbol_list

def stock_price(ticker):
	""" Function gets share chart 5y"""
	req = r.get(iex_base_url+"stock/"+ ticker +"/chart/5y")
	prices = req.json()
	return prices

def get_stock_company(ticker):
    """ Function gets company details from IEX API """
    stock_comp = "/stock/" + ticker + "/company"
    ticker_comp = r.get(iex_base_url+stock_comp)
    comp = ticker_comp.json()
    return comp

def get_stock_logo(ticker):
    """ Function retrieves logo from IEX """
    stock_logo_url = "/stock/" + ticker + "/logo"
    ticker_logo = r.get(iex_base_url+stock_logo_url)
    logo = ticker_logo.json()
    return logo['url']