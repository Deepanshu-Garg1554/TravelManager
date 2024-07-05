from django.contrib import admin
from  .models import Destination
from .models import Detailed_desc,hotels,Booking,flight
# Register your models here.

admin.site.register(Destination)
admin.site.register(Detailed_desc)
admin.site.register(hotels)
admin.site.register(Booking)
admin.site.register(flight)