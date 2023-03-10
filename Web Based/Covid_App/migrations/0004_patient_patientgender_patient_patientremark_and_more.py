# Generated by Django 4.1.1 on 2022-11-24 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pneumonia_App', '0003_alter_patient_patient_x_ray_heatmap'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='PatientGender',
            field=models.CharField(default='M', max_length=2),
        ),
        migrations.AddField(
            model_name='patient',
            name='PatientRemark',
            field=models.CharField(default='Home Qurantine', max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='PatientStatus',
            field=models.CharField(default='Covid', max_length=20),
        ),
    ]
