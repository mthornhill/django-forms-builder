# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Form.name'
        db.add_column(u'forms_form', 'name',
                      self.gf('django.db.models.fields.CharField')(default='name placeholder', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Form.name'
        db.delete_column(u'forms_form', 'name')


    models = {
        u'forms.field': {
            'Meta': {'ordering': "(u'order',)", 'object_name': 'Field'},
            'choices': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'field_type': ('django.db.models.fields.IntegerField', [], {}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'fields'", 'to': u"orm['forms.Form']"}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'placeholder_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'fields'", 'null': 'True', 'to': u"orm['forms.Section']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "u''", 'max_length': '100', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'forms.fieldentry': {
            'Meta': {'object_name': 'FieldEntry'},
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'fields'", 'to': u"orm['forms.FormEntry']"}),
            'field_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'})
        },
        u'forms.form': {
            'Meta': {'object_name': 'Form'},
            'button_text': ('django.db.models.fields.CharField', [], {'default': "u'Submit'", 'max_length': '50'}),
            'email_copies': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email_from': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'email_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email_subject': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'redirect_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'response': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'send_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'default': '[1]', 'related_name': "u'forms_form_forms'", 'symmetrical': 'False', 'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'forms.formentry': {
            'Meta': {'object_name': 'FormEntry'},
            'entry_time': ('django.db.models.fields.DateTimeField', [], {}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'entries'", 'to': u"orm['forms.Form']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'forms.section': {
            'Meta': {'object_name': 'Section'},
            'form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'sections'", 'to': u"orm['forms.Form']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['forms']