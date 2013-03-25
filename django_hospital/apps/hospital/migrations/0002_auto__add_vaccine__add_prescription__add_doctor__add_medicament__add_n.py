# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vaccine'
        db.create_table(u'hospital_vaccine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('live', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('absorved', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('inactivated', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('oral', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'hospital', ['Vaccine'])

        # Adding model 'Prescription'
        db.create_table(u'hospital_prescription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hospital.Visit'])),
            ('medicament', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hospital.Medicament'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'hospital', ['Prescription'])

        # Adding model 'Doctor'
        db.create_table(u'hospital_doctor', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('specialty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hospital.DoctorSpeciality'])),
            ('certification', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'hospital', ['Doctor'])

        # Adding model 'Medicament'
        db.create_table(u'hospital_medicament', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('grs', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'hospital', ['Medicament'])

        # Adding model 'Nurse'
        db.create_table(u'hospital_nurse', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('specialty', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hospital.NurseSpeciality'], unique=True)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'hospital', ['Nurse'])

        # Adding model 'Patient'
        db.create_table(u'hospital_patient', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('ssn', self.gf('django.db.models.fields.CharField')(unique=True, max_length=9)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'hospital', ['Patient'])

        # Adding model 'NurseSpeciality'
        db.create_table(u'hospital_nursespeciality', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('specialty', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'hospital', ['NurseSpeciality'])

        # Adding model 'Visit'
        db.create_table(u'hospital_visit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hospital.Patient'])),
            ('doctor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hospital.Doctor'])),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal(u'hospital', ['Visit'])

        # Adding model 'VaccineApplied'
        db.create_table(u'hospital_vaccineapplied', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('vaccine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hospital.Vaccine'])),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hospital.Patient'])),
            ('nurse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hospital.Nurse'])),
        ))
        db.send_create_signal(u'hospital', ['VaccineApplied'])

        # Adding model 'MedPrice'
        db.create_table(u'hospital_medprice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('medicament', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hospital.Medicament'])),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'hospital', ['MedPrice'])

        # Adding model 'Department'
        db.create_table(u'hospital_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('director', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'hospital', ['Department'])

        # Adding M2M table for field staff on 'Department'
        db.create_table(u'hospital_department_staff', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('department', models.ForeignKey(orm[u'hospital.department'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(u'hospital_department_staff', ['department_id', 'user_id'])

        # Adding model 'DoctorSpeciality'
        db.create_table(u'hospital_doctorspeciality', (
            ('specialty', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
        ))
        db.send_create_signal(u'hospital', ['DoctorSpeciality'])


    def backwards(self, orm):
        # Deleting model 'Vaccine'
        db.delete_table(u'hospital_vaccine')

        # Deleting model 'Prescription'
        db.delete_table(u'hospital_prescription')

        # Deleting model 'Doctor'
        db.delete_table(u'hospital_doctor')

        # Deleting model 'Medicament'
        db.delete_table(u'hospital_medicament')

        # Deleting model 'Nurse'
        db.delete_table(u'hospital_nurse')

        # Deleting model 'Patient'
        db.delete_table(u'hospital_patient')

        # Deleting model 'NurseSpeciality'
        db.delete_table(u'hospital_nursespeciality')

        # Deleting model 'Visit'
        db.delete_table(u'hospital_visit')

        # Deleting model 'VaccineApplied'
        db.delete_table(u'hospital_vaccineapplied')

        # Deleting model 'MedPrice'
        db.delete_table(u'hospital_medprice')

        # Deleting model 'Department'
        db.delete_table(u'hospital_department')

        # Removing M2M table for field staff on 'Department'
        db.delete_table('hospital_department_staff')

        # Deleting model 'DoctorSpeciality'
        db.delete_table(u'hospital_doctorspeciality')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hospital.department': {
            'Meta': {'object_name': 'Department'},
            'director': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'staff': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        },
        u'hospital.doctor': {
            'Meta': {'object_name': 'Doctor'},
            'certification': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'specialty': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hospital.DoctorSpeciality']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'hospital.doctorspeciality': {
            'Meta': {'object_name': 'DoctorSpeciality'},
            'specialty': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'})
        },
        u'hospital.medicament': {
            'Meta': {'object_name': 'Medicament'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'grs': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'hospital.medprice': {
            'Meta': {'object_name': 'MedPrice'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medicament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hospital.Medicament']"}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        },
        u'hospital.nurse': {
            'Meta': {'object_name': 'Nurse'},
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'specialty': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hospital.NurseSpeciality']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'hospital.nursespeciality': {
            'Meta': {'object_name': 'NurseSpeciality'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'specialty': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'hospital.patient': {
            'Meta': {'object_name': 'Patient'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'ssn': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '9'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'hospital.prescription': {
            'Meta': {'object_name': 'Prescription'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'medicament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hospital.Medicament']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'visit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hospital.Visit']"})
        },
        u'hospital.vaccine': {
            'Meta': {'object_name': 'Vaccine'},
            'absorved': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inactivated': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'live': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'oral': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'hospital.vaccineapplied': {
            'Meta': {'object_name': 'VaccineApplied'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nurse': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hospital.Nurse']"}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hospital.Patient']"}),
            'vaccine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hospital.Vaccine']"})
        },
        u'hospital.visit': {
            'Meta': {'object_name': 'Visit'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hospital.Doctor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hospital.Patient']"})
        }
    }

    complete_apps = ['hospital']