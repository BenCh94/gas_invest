from django.urls import path, re_path

from . import views
from django.contrib.auth import views as auth_views 

app_name = 'gas_dash'
urlpatterns = [
	# This is the home dashboard '/gas_dash'
    path('', views.index, name='index'),
    # The registration view
    re_path(r'^signup/$', views.signup, name='signup'),
    # This is the login page
    re_path(r'^login/$', auth_views.login, name='login'),
    # The logout page
    re_path(r'^logout/$', auth_views.logout, {'next_page': '/'},  name='logout'),
    # Add a stock
    path('stocks/add', views.add_stock, name='add_stock'),
    # This is a stock page '/gas_dash/<stock_id>'
    path('stocks/<int:stock_id>', views.stock, name='stock'),
    # This is a stock trades page '/gas_dash/<stock_id>/trades'
    path('stocks/<int:stock_id>/trades', views.trades, name='trades'),
    # This is a trade page '/gas_dash/<trade_id>'
    path('trade/<int:stock_id>', views.trade, name='trade')
]
