# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Doctor'
        db.create_table(u'hospital_doctor', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('specialty', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hospital.DoctorSpeciality'], unique=True)),
            ('certification', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'hospital', ['Doctor'])

        # Adding model 'Medicament'
        db.create_table(u'hospital_medicament', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'hospital', ['Medicament'])

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

        # Adding model 'Patient'
        db.create_table(u'hospital_patient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ssn', self.gf('django.db.models.fields.CharField')(unique=True, max_length=9)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'hospital', ['Patient'])

        # Adding model 'NurseSpeciality'
        db.create_table(u'hospital_nursespeciality', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('specialty', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'hospital', ['NurseSpeciality'])

        # Adding model 'Visit'
        db.create_table(u'hospital_visit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hospital.Patient'])),
            ('provider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hospital.Doctor'])),
        ))
        db.send_create_signal(u'hospital', ['Visit'])

        # Adding model 'Nurse'
        db.create_table(u'hospital_nurse', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('specialty', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['hospital.NurseSpeciality'], unique=True)),
        ))
        db.send_create_signal(u'hospital', ['Nurse'])

        # Adding model 'DoctorSpeciality'
        db.create_table(u'hospital_doctorspeciality', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('specialty', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'hospital', ['DoctorSpeciality'])


    def backwards(self, orm):
        # Deleting model 'Doctor'
        db.delete_table(u'hospital_doctor')

        # Deleting model 'Medicament'
        db.delete_table(u'hospital_medicament')

        # Deleting model 'Department'
        db.delete_table(u'hospital_department')

        # Removing M2M table for field staff on 'Department'
        db.delete_table('hospital_department_staff')

        # Deleting model 'Patient'
        db.delete_table(u'hospital_patient')

        # Deleting model 'NurseSpeciality'
        db.delete_table(u'hospital_nursespeciality')

        # Deleting model 'Visit'
        db.delete_table(u'hospital_visit')

        # Deleting model 'Nurse'
        db.delete_table(u'hospital_nurse')

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
            'specialty': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hospital.DoctorSpeciality']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'hospital.doctorspeciality': {
            'Meta': {'object_name': 'DoctorSpeciality'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'specialty': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'hospital.medicament': {
            'Meta': {'object_name': 'Medicament'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        u'hospital.nurse': {
            'Meta': {'object_name': 'Nurse'},
            'specialty': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['hospital.NurseSpeciality']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'hospital.nursespeciality': {
            'Meta': {'object_name': 'NurseSpeciality'},
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'specialty': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'hospital.patient': {
            'Meta': {'object_name': 'Patient'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ssn': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '9'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'hospital.visit': {
            'Meta': {'object_name': 'Visit'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hospital.Patient']"}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hospital.Doctor']"})
        }
    }

    complete_apps = ['hospital']