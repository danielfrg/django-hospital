from django.contrib.auth.models import User, AbstractBaseUser
from django.contrib import admin
from django.db import models
from django import forms

class Patient(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    ssn = models.CharField(max_length=9, unique=True)
    birthday = models.DateField()
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=5)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name

class PatientAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    search_fields = ('user__first_name', 'user__last_name', 'user__ssn')
    list_display = ('__unicode__', 'birthday', 'ssn', )

# --

class DoctorSpeciality(models.Model):
    specialty = models.CharField(max_length=30, primary_key=True)

    def __unicode__(self):
        return self.specialty

class DoctorSpecialityAdmin(admin.ModelAdmin):
    search_fields = ('specialty', )

class Doctor(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    specialty = models.ForeignKey(DoctorSpeciality)

    certification_CHOICES = (
        ('A', 'American Board'),
        ('B', 'Bachelor'),
    )
    certification = models.CharField(max_length=30, choices=certification_CHOICES)

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name

class DoctorAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    search_fields = ('user__first_name', 'user__last_name', )
    list_filter = ('specialty', )
    list_display = ('__unicode__', 'specialty')

# --

class NurseSpeciality(models.Model):
    specialty = models.CharField(max_length=60)

    def __unicode__(self):
        return self.specialty

class NurseSpecialityAdmin(admin.ModelAdmin):
    search_fields = ('specialty', )

class Nurse(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    specialty = models.OneToOneField(NurseSpeciality)
    degree_CHOICES = (
        ('A', 'Associate Degree in Nursing'),
        ('D', 'Diploma in Nursing'),
        ('L', 'Licensed Practical Nurse'),
        ('AD', 'Advanced practice registered nurses'),
    )
    degree = models.CharField(max_length=30, choices=degree_CHOICES)

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name

class NurseAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    search_fields = ('user__first_name', )
    list_filter = ('specialty', 'degree')
    list_display = ('__unicode__', 'specialty')

# --

class Medicament(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    grs = models.IntegerField()

    def __unicode__(self):
        return self.name

class MedicamentsForm( forms.ModelForm ):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Medicament

class MedicamentAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'grs')
    form = MedicamentsForm

class MedPrice(models.Model):
    date = models.DateTimeField()
    medicament = models.ForeignKey(Medicament)
    price = models.IntegerField()

    def __unicode__(self):
        return '%s (%s)' % (self.medicament.name, self.date)

class MedPriceAdmin(admin.ModelAdmin):
    raw_id_fields = ('medicament', )
    search_fields = ('medicament', )
    list_display = ('medicament', 'price', 'date')

# --

class Visit(models.Model):
    date = models.DateTimeField()
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    comments = models.CharField(max_length=2000)

    def __unicode__(self):
        return '%s | by  %s (%s)' % (self.patient, self.doctor, self.date)

class VisitForm(forms.ModelForm):
    comments = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Visit

class VisitAdmin(admin.ModelAdmin):
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__user__first_name', 'doctor__user__last_name')
    raw_id_fields = ('patient', 'doctor')
    list_display = ('patient', 'doctor', 'date')
    list_display_links = ('patient', 'doctor')
    form = VisitForm

# --

class Prescription(models.Model):
    visit = models.ForeignKey(Visit)
    medicament = models.ForeignKey(Medicament)
    quantity = models.IntegerField()
    length = models.IntegerField()

    def __unicode__(self):
        return '%s | Prescribed by: %s (%s)' % (self.visit.patient, self.visit.doctor, self.visit.date)

class PrescriptionAdmin(admin.ModelAdmin):
    search_fields = ('medicament__name', 'visit__patient__last_name', 'visit__patient__first_name', 
                    'visit__doctor__user__last_name', 'visit__doctor__user__first_name')
    raw_id_fields = ('visit', 'medicament', )
    list_display = ('visit', 'medicament', 'quantity', 'length')
    # list_display_links = ('patient', 'medicament', 'doctor')

# --

class Department(models.Model):
    name = models.CharField(max_length=10)
    director = models.OneToOneField(User)
    staff = models.ManyToManyField(User, related_name='+')

    def __unicode__(self):
        return self.name

class DepartmentAdmin(admin.ModelAdmin):
    filter_horizontal = ('staff', )

# --

class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    live = models.NullBooleanField()
    absorved = models.NullBooleanField()
    inactivated = models.NullBooleanField()
    oral = models.NullBooleanField()

    def __unicode__(self):
        return self.name

class VaccineAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'live', 'absorved', 'inactivated', 'oral')
    list_filter = ('live', 'absorved', 'inactivated', 'oral', )

class VaccineApplied(models.Model):
    date = models.DateTimeField()
    vaccine = models.ForeignKey(Vaccine)
    patient = models.ForeignKey(Patient)
    nurse = models.ForeignKey(Nurse)
    
    def __unicode__(self):
        return '%s | by  %s (%s)' % (self.patient, self.nurse, self.date)

class VaccineAppliedAdmin(admin.ModelAdmin):
    search_fields = ('vaccine__name', 'patient__user__last_name', 'patient__user__first_name', 
                'nurse__user__last_name', 'nurse__user__first_name')
    list_display = ('patient', 'nurse', 'vaccine', 'date')
    raw_id_fields = ('patient', 'nurse', 'vaccine', )
    list_display_links = ('patient', 'nurse',)




