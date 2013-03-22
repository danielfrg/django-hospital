from django.contrib import admin
from models import *

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Nurse, NurseAdmin)
admin.site.register(DoctorSpeciality, DoctorSpecialityAdmin)
admin.site.register(NurseSpeciality, NurseSpecialityAdmin)

admin.site.register(Department)

admin.site.register(Medicament, MedicamentAdmin)
admin.site.register(MedPrice, MedPriceAdmin)
admin.site.register(Visit, VisitAdmin)
admin.site.register(Patient, PatientAdmin)

