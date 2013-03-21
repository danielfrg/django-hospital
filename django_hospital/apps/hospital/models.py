from django.contrib.auth.models import User, AbstractBaseUser
from django.db import models

class Patient(models.Model):
    ssn = models.CharField(max_length=9, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    email = models.EmailField()
    street = models.CharField(max_length=30)
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

class DoctorSpeciality(models.Model):
    specialty = models.CharField(max_length=30)

    def __unicode__(self):
        return self.specialty

class Doctor(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    specialty = models.OneToOneField(DoctorSpeciality)

    certification_CHOICES = (
        ('A', 'American Board'),
        ('B', 'Bachelor'),
    )
    certification = models.CharField(max_length=30, choices=certification_CHOICES)

    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name

class NurseSpeciality(models.Model):
    specialty = models.CharField(max_length=60)

    def __unicode__(self):
        return self.specialty

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

class Visit(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(Patient)
    provider = models.ForeignKey(Doctor)


class Department(models.Model):
    name = models.CharField(max_length=10)
    director = models.OneToOneField(User)
    staff = models.ManyToManyField(User, related_name='+')

    def __unicode__(self):
        return self.name

class Medicament(models.Model):
    name = models.CharField(max_length=150)
    grs = models.IntegerField()






