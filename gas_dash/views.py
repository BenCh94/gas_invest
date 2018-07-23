from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from gas_dash.forms import SignUpForm
from django.http import Http404
from .models import Stock

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
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='/gas_dash/login/')
def index(request):
	current_user = request.user
	profile = current_user.profile
	stocks = Stock.objects.filter(user_profile=profile)
	context = {'stocks': stocks}
	return render(request, 'gas_dash/dashboard.html', context)

@login_required(login_url='/gas_dash/login/')
def add_stock(request):
	current_user = request.user
	profile = current_user.profile
	return render(request, 'gas_dash/add_stock.html')

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
