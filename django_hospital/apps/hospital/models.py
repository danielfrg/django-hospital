from django.contrib.auth.models import User, AbstractBaseUser
from django.contrib import admin
from django.db import models
from django import forms

class Patient(models.Model):
    ssn = models.CharField(max_length=9, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    email = models.EmailField()
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
        return self.first_name + " " + self.last_name

class PatientAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'ssn')
    list_display = ('first_name', 'last_name', 'email', 'ssn')

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
        return self.user.first_name + " " + self.user.last_name

class DoctorAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",)
    search_fields = ('user__last_name', )
    list_filter = ('specialty', )
    list_display = ('__unicode__', 'specialty')

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
        return self.user.first_name + " " + self.user.last_name

class NurseAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    search_fields = ('user__first_name', )
    list_filter = ('specialty', 'degree')
    list_display = ('__unicode__', 'specialty')

class Visit(models.Model):
    date = models.DateTimeField()
    patient = models.ForeignKey(Patient)
    provider = models.ForeignKey(Doctor)

class VisitAdmin(admin.ModelAdmin):
    raw_id_fields = ('patient', 'provider')
    list_display = ('patient', 'provider', 'date')
    list_display_links = ('patient', 'provider')


class Medicament(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    grs = models.IntegerField()

    def __unicode__(self):
        return self.name

class MedicamentsForm( forms.ModelForm ):
    description = forms.CharField( widget=forms.Textarea )
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

class MedPriceAdmin(admin.ModelAdmin):
    raw_id_fields = ('medicament', )
    search_fields = ('medicament', )
    list_display = ('medicament', 'price', 'date')


class Department(models.Model):
    name = models.CharField(max_length=10)
    director = models.OneToOneField(User)
    staff = models.ManyToManyField(User, related_name='+')

    def __unicode__(self):
        return self.name

