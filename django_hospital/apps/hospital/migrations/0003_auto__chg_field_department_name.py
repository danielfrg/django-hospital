# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Department.name'
        db.alter_column(u'hospital_department', 'name', self.gf('django.db.models.fields.CharField')(max_length=30))

    def backwards(self, orm):

        # Changing field 'Department.name'
        db.alter_column(u'hospital_department', 'name', self.gf('django.db.models.fields.CharField')(max_length=10))

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
            'director': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
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