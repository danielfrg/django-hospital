#encode UTF-8
from django.http import HttpResponse
from django.template import Context, loader

from models import *


def index(request):
    return HttpResponse("Index <a href='/admin'>admin</a>")
    template = loader.get_template('index.html')
    context = Context({
    })
    return HttpResponse(template.render(context))


import random
from faker import Factory
from django.contrib.auth.models import User, Group
from lists import *

def generate(request):
    cnt = ''
    cnt += '<a href="/generate/doctor">doctor</a></br>'
    cnt += '<a href="/generate/nurse">nurse</a></br>'
    cnt += '<a href="/generate/patient">patient</a></br>'
    cnt += '<a href="/generate/dbadmin">dbadmin</a></br>'
    cnt += '----------------------------</br>'
    cnt += '<a href="/generate/meds">meds</a></br>'
    cnt += '<a href="/generate/specialities">specialities</a></br>'
    cnt += '<a href="/generate/groups">group</a></br>'
    return HttpResponse(cnt)

    url(r'^generate/groups$', views.generate_groups),
    url(r'^generate/specialities$', views.generate_specialities),
    url(r'^generate/doctor$', views.generate_doctor),
    url(r'^generate/nurse$', views.generate_nurse),
    url(r'^generate/patient$', views.generate_patient),
    url(r'^generate/dbadmin$', views.generate_dbadmin),

def generate_doctor(request):
    fake = Factory.create()
    first_name = fake.firstName()
    email = fake.companyEmail()
    user = User.objects.create_user(first_name, email, 'doctor-pass')
    user.first_name = first_name
    user.last_name = fake.lastName()
    user.is_staff = True

    g = Group.objects.get(name='Doctor') 
    g.user_set.add(user)
    user.save()

    new = Doctor()
    new.user = user
    specialities = DoctorSpeciality.objects.all()
    new.specialty = specialities[int(random.random() * len(specialities))]
    new.certification = 'A' if random.random() > 0.5 else 'B'
    new.save()
    return HttpResponse(':)')

def generate_nurse(request):
    fake = Factory.create()
    first_name = fake.firstName()
    email = fake.companyEmail()
    user = User.objects.create_user(first_name, email, 'nurse-pass')
    user.first_name = first_name
    user.last_name = fake.lastName()
    user.is_staff = True

    g = Group.objects.get(name='Nurse') 
    g.user_set.add(user)
    user.save()

    new = Nurse()
    new.user = user
    specialities = NurseSpeciality.objects.all()
    new.specialty = specialities[int(random.random() * len(specialities))]
    new.degree = 'A' if random.random() > 0.5 else 'AD'
    new.save()
    return HttpResponse(':)')

def generate_dbadmin(request):
    fake = Factory.create()
    first_name = fake.firstName()
    email = fake.companyEmail()
    new = User.objects.create_user(first_name, email, 'admin-pass')
    new.first_name = first_name
    new.last_name = fake.lastName()
    new.is_staff = True
    new.is_superuser = True

    g = Group.objects.get(name='DBAdmin') 
    g.user_set.add(new)
    
    new.save()
    return HttpResponse(':)')

def generate_patient(request):
    fake = Factory.create()
    new = Patient()
    new.ssn = int(random.random() * 999999999)
    new.first_name = fake.firstName()
    new.last_name = fake.lastName()
    new.birthday = fake.date()
    new.gender = 'M' if random.random() > 0.5 else 'F'
    new.email = fake.freeEmail()
    new.street = fake.streetAddress()
    new.state = fake.state()
    new.city = fake.city()
    new.zip_code = int(random.random() * 75555)
    
    new.save()
    return HttpResponse(':)')

def generate_meds(request):
    for m in meds:
        new = Medicament()
        new.name = m
        new.grs = int(random.random() * 100)
        new.save()
    return HttpResponse(':))')

def generate_groups(request):
    groups = ['Doctor', 'Nurse', 'Admin', 'Tech']
    for g in groups:
        new = Group()
        new.name = g
        new.save()
    return HttpResponse(':))')

def generate_specialities(request):
    for sp in doctor_specialities:
        s = DoctorSpeciality()
        s.specialty = sp
        s.save()

    for sp in nurse_specialities:
        s = NurseSpeciality()
        s.specialty = sp
        s.save()

    return HttpResponse(':))')
