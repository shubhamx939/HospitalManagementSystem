from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Appointment)
admin.site.register(BloodBank)
admin.site.register(Medicine)
admin.site.register(MedicineSales)