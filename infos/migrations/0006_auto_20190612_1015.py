# Generated by Django 2.2 on 2019-06-12 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0005_topic_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
