import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
	    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()


class Stock(models.Model):
	StockStatuses = [('a', 'Active'), ('i', 'Inactive')]
	user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
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


