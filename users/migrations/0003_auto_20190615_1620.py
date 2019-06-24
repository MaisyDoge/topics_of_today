# Generated by Django 2.2 on 2019-06-15 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0010_topic_views'),
        ('users', '0002_auto_20190611_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='topic1',
            field=models.ForeignKey(default=1, on_delete=None, related_name='topic1', to='infos.Topic'),
        ),
        migrations.AddField(
            model_name='profile',
            name='topic2',
            field=models.ForeignKey(default=2, on_delete=None, related_name='topic2', to='infos.Topic'),
        ),
        migrations.AddField(
            model_name='profile',
            name='topic3',
            field=models.ForeignKey(default=3, on_delete=None, related_name='topic3', to='infos.Topic'),
        ),
    ]