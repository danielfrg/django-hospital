from django.contrib import admin
from models import *

admin.site.register(Patient)
admin.site.register(Visit)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(DoctorSpeciality)
admin.site.register(NurseSpeciality)

admin.site.register(Department)
admin.site.register(Medicament)

