# username HMS
# gmail hms@gmail.com
# password 12345678910
# Register your models here.

# username GroupProject
# gmail GP@gmail.com
# password 9022381054

# Register your models here.

from django.contrib import admin
from .models import Doctor,Patient,Inpatient,Outpatient

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Inpatient)
admin.site.register(Outpatient)
