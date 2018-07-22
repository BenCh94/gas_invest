from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Stock

# Create your views here.
def index(request):
	stocks = Stock.objects.all()
	context = {'stocks': stocks}
	return render(request, 'gas_dash/dashboard.html', context)

def stock(request, stock_id):
	stock = get_object_or_404(Stock, pk=stock_id)
	return render(request, 'gas_dash/stock_detail.html', {'stock': stock})

def trades(request, stock_id):
	return HttpResponse("You're looking at trades for %s." % stock_id)

def trade(request, trade_id):
	return HttpResponse("You're looking at trade %s." % trade_id)
