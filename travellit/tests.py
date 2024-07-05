from django.test import TestCase
from datetime import datetime, timedelta

from django.urls import reverse
from .models import hotels
from .models import flight
class HotelsModelTestCase(TestCase):
    def setUp(self):
        self.hotel = hotels.objects.create(
            name='Sample Hotel',
            room=10,
            price=100,
            city='Sample City',
            check_in_date=datetime.now(),
            check_out_date=datetime.now()
        )

    def test_hotel_creation(self):
        """Test the creation of a hotel instance"""
        self.assertEqual(self.hotel.name, 'Sample Hotel')
        self.assertEqual(self.hotel.room, 10)
        self.assertEqual(self.hotel.price, 100)
        self.assertEqual(self.hotel.city, 'Sample City')
        self.assertIsInstance(self.hotel.check_in_date, datetime)
        self.assertIsInstance(self.hotel.check_out_date, datetime)

class FlightModelTestCase(TestCase):
    def test_flight_creation(self):
        flight1 = flight.objects.create(
            name='Test Flight',
            price=100,
            from_city='City A',
            to_city='City B',
            depart=datetime.strptime('2024-05-05', '%Y-%m-%d').date()
        )
        saved_flight = flight.objects.get(name='Test Flight')
        self.assertEqual(saved_flight.name, 'Test Flight')
        self.assertEqual(saved_flight.price, 100)
        self.assertEqual(saved_flight.from_city, 'City A')
        self.assertEqual(saved_flight.to_city, 'City B')
        self.assertEqual(saved_flight.depart, datetime.strptime('2024-05-05', '%Y-%m-%d').date())
        self.assertTrue(flight.objects.filter(name='Test Flight').exists())

