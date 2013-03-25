from django.contrib import admin
from models import *

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Nurse, NurseAdmin)
admin.site.register(DoctorSpeciality, DoctorSpecialityAdmin)
admin.site.register(NurseSpeciality, NurseSpecialityAdmin)


admin.site.register(Medicament, MedicamentAdmin)
admin.site.register(MedPrice, MedPriceAdmin)
admin.site.register(Prescription, PrescriptionAdmin)

admin.site.register(Vaccine, VaccineAdmin)
admin.site.register(VaccineApplied, VaccineAppliedAdmin)

admin.site.register(Visit, VisitAdmin)
admin.site.register(Patient, PatientAdmin)

