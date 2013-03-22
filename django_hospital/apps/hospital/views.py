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
import datetime

def generate(request):
    cnt = ''
    cnt += '<a href="/generate/doctor">doctor</a></br>'
    cnt += '<a href="/generate/nurse">nurse</a></br>'
    cnt += '<a href="/generate/dbadmin">dbadmin</a></br>'
    cnt += '<a href="/generate/patient">patient</a></br>'
    cnt += '<a href="/generate/visit">visit</a></br>'
    cnt += '<a href="/generate/med_price">med price</a></br>'
    cnt += '</br>'
    cnt += '-------------------------------</br>'
    cnt += 'After initializing the database</br>'
    cnt += '<a href="/generate/meds">meds</a></br>'
    cnt += '<a href="/generate/specialities">specialities</a></br>'
    cnt += '<a href="/generate/groups">groups</a></br>'
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
    last_name = fake.lastName()
    username = first_name + '.' + last_name
    email = username + '@goodhospital.com'
    user = User.objects.create_user(username, email, 'doctor-pass')
    user.first_name = first_name
    user.last_name = last_name
    user.is_staff = True

    g = Group.objects.get(name='Doctor') 
    g.user_set.add(user)

    new = Doctor()
    new.user = user
    specialities = DoctorSpeciality.objects.all()
    new.specialty = specialities[int(random.random() * len(specialities))]
    new.certification = 'A' if random.random() > 0.5 else 'B'

    user.save()
    new.save()
    return HttpResponse(':)')

def generate_nurse(request):
    fake = Factory.create()
    first_name = fake.firstName()
    last_name = fake.lastName()
    username = first_name + '.' + last_name
    email = username + '@goodhospital.com'
    user = User.objects.create_user(username, email, 'nurse-pass')
    user.first_name = first_name
    user.last_name = last_name
    user.is_staff = True

    g = Group.objects.get(name='Nurse') 
    g.user_set.add(user)

    new = Nurse()
    new.user = user
    specialities = NurseSpeciality.objects.all()
    new.specialty = specialities[int(random.random() * len(specialities))]
    new.degree = 'A' if random.random() > 0.5 else 'AD'

    user.save()
    new.save()
    return HttpResponse(':)')

def generate_dbadmin(request):
    fake = Factory.create()
    first_name = fake.firstName()
    last_name = fake.lastName()
    username = first_name + '.' + last_name
    email = username + '@goodhospital.com'
    user = User.objects.create_user(username, email, 'admin-pass')
    user.first_name = first_name
    user.last_name = fake.lastName()
    user.is_staff = True
    user.is_superuser = True

    g = Group.objects.get(name='DB Admin') 
    g.user_set.add(user)
    
    user.save()
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

def generate_visit(request):
    patients = Patient.objects.all()
    patient = patients[int(random.random() * len(patients))]

    doctors = Doctor.objects.all()
    doctor = doctors[int(random.random() * len(doctors))]

    visit = Visit()
    visit.patient = patient
    visit.provider = doctor
    visit.date = datetime.datetime.now()
    visit.save()
    return HttpResponse(':)')

def generate_meds(request):
    fake = Factory.create()
    for m in meds:
        new = Medicament()
        new.name = m
        new.grs = int(random.random() * 100) + 5
        new.description = fake.paragraph()
        new.save()
    return HttpResponse(':)')

def generate_med_price(request):
    meds = Medicament.objects.all()
    med = meds[int(random.random() * len(meds))]
    price = MedPrice()
    price.date = datetime.datetime.now()
    price.medicament = med
    price.price = random.random() * 100 + 10
    price.save()

    return HttpResponse(':)')


def generate_groups(request):
    groups = ['Doctor', 'Head Doctor', 'Nurse', 'Head Nurse', 'Sales', 'DB Admin']
    for g in groups:
        new = Group()
        new.name = g
        new.save()
    return HttpResponse(':)')

def generate_specialities(request):
    for sp in doctor_specialities:
        s = DoctorSpeciality()
        s.specialty = sp
        s.save()

    for sp in nurse_specialities:
        s = NurseSpeciality()
        s.specialty = sp
        s.save()

    return HttpResponse(':)')
