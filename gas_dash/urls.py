from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = 'gas_dash'
urlpatterns = [
	# This is the home dashboard '/gas_dash'
    path('', views.index, name='index'),
    # This is the login page
    path(r'^login/$', auth_views.login, name='login'),
    # This is a stock page '/gas_dash/<stock_id>'
    path('stocks/<int:stock_id>', views.stock, name='stock'),
    # This is a stock trades page '/gas_dash/<stock_id>/trades'
    path('stocks/<int:stock_id>/trades', views.trades, name='trades'),
    # This is a trade page '/gas_dash/<trade_id>'
    path('trade/<int:stock_id>', views.trade, name='trade')
]
