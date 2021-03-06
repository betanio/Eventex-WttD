# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Subscription.paid'
        db.add_column('subscriptions_subscription', 'paid',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Subscription.phone'
        db.alter_column('subscriptions_subscription', 'phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Subscription.email'
        db.alter_column('subscriptions_subscription', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75, unique=True, null=True))
    def backwards(self, orm):
        # Deleting field 'Subscription.paid'
        db.delete_column('subscriptions_subscription', 'paid')


        # Changing field 'Subscription.phone'
        db.alter_column('subscriptions_subscription', 'phone', self.gf('django.db.models.fields.CharField')(default='', max_length=20))

        # Changing field 'Subscription.email'
        db.alter_column('subscriptions_subscription', 'email', self.gf('django.db.models.fields.EmailField')(default='', max_length=75, unique=True))
    models = {
        'subscriptions.subscription': {
            'Meta': {'ordering': "['created_at']", 'object_name': 'Subscription'},
            'cpf': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'unique': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'})
        }
    }

    complete_apps = ['subscriptions']