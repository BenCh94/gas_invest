from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Stock

# Create your views here.
@login_required(login_url='/gas_dash/login/')
def index(request):
	stocks = Stock.objects.all()
	context = {'stocks': stocks}
	return render(request, 'gas_dash/dashboard.html', context)

@login_required()
def stock(request, stock_id):
	stock = get_object_or_404(Stock, pk=stock_id)
	return render(request, 'gas_dash/stock_detail.html', {'stock': stock})

@login_required()
def trades(request, stock_id):
	return HttpResponse("You're looking at trades for %s." % stock_id)

@login_required()
def trade(request, trade_id):
	stocks = Stock.objects.all()
	return HttpResponse("You're looking at trade %s." % trade_id)
