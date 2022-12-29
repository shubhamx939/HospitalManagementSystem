from django.contrib import admin

from .models import *

admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Pharmacist)
admin.site.register(Labouratorist)
admin.site.register(Accountant)