# Generated by Django 3.1.2 on 2020-12-27 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='topic',
            field=models.CharField(default='NEW', max_length=50),
        ),
    ]
