# Generated by Django 3.1.3 on 2020-11-19 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientdb', '0002_signals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='record_name',
            field=models.IntegerField(),
        ),
    ]
