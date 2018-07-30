from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import SignUpForm, StockForm
from .models import Stock, Trade
from .iex_requests import *

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        signup_form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': signup_form})

@login_required(login_url='/gas_dash/login/')
def index(request):
	""" The home dashboards view """
	current_user = request.user
	profile = current_user.profile
	stocks = Stock.objects.filter(user_profile=profile)
	context = {'stocks': stocks}
	return render(request, 'gas_dash/dashboard.html', context)

@login_required(login_url='/gas_dash/login/')
def add_stock(request):
	""" Function for adding a new stock to the dashboard: limited to stocks on IEX """
	symbols = list_symbols()
	current_user = request.user
	profile = current_user.profile
	stock_form = StockForm()
	return render(request, 'gas_dash/add_stock.html', {'form': stock_form, 'symbols': symbols})

@login_required(login_url='/gas_dash/login/')
def stock(request, stock_id):
	stock = get_object_or_404(Stock, pk=stock_id)
	return render(request, 'gas_dash/stock_detail.html', {'stock': stock})

@login_required(login_url='/gas_dash/login/')
def trades(request, stock_id):
	return HttpResponse("You're looking at trades for %s." % stock_id)

@login_required(login_url='/gas_dash/login/')
def trade(request, trade_id):
	stocks = Stock.objects.all()
	return HttpResponse("You're looking at trade %s." % trade_id)
