import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Stock(models.Model):
	StockStatuses = [('a', 'Active'), ('i', 'Inactive')]
	name = models.CharField(max_length=200)
	ticker = models.CharField(max_length=10)
	quantity = models.IntegerField()
	invested = models.FloatField()
	fees_usd = models.FloatField()
	start_date = models.DateTimeField()
	status = models.CharField(max_length=2, choices=StockStatuses)
	def __str__(self):
		return self.name



class Trade(models.Model):
	TradeTypes = [('b', 'Buy'), ('s','Sell')]
	stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
	date = models.DateTimeField()
	trade_type = models.CharField(max_length=2, choices=TradeTypes)
	amount = models.FloatField()
	fees_usd = models.FloatField()
	avg_price = models.FloatField()
	def __str__(self):
		return self.avg_price


