import datetime

from django.test import TestCase
from django.utils import timezone

from ..models import Stock, User, Trade, Profile
# Create your tests here.


class StockModelTests(TestCase):

    def setUp(self):
        """
        Setup mocks for testing
        """
        user_one = User.objects.create(username='Tester1', first_name='John', last_name='Test', email='john@test.com')
        user_one.profile.bio = "I'm John and I'm here to test..."
        Stock.objects.create(user_profile=user_one.profile, 
        					name='test_stock', 
        					ticker='tst', 
        					quantity=1, 
        					invested=100,
        					fees_usd=2.99,
        					start_date=timezone.now(),
        					status='a')

    def test_user_owns_stock(self):
    	""" Stock assigned to user profile belongs to that user """
    	stock = Stock.objects.get(name='test_stock')
    	user = User.objects.get(username='Tester1')
    	self.assertEqual(stock.user_profile, user.profile)

