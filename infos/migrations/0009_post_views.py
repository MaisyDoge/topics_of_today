# Generated by Django 2.2 on 2019-06-15 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0008_auto_20190612_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
