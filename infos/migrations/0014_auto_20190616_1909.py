# Generated by Django 2.2 on 2019-06-17 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0013_alert_href'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
    ]
