# Generated by Django 4.2.10 on 2024-06-22 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HMS_App', '0002_patient_rename_dr_name_doctor_dr_name_inpatient_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='Dr_Specilization',
            new_name='Dr_Specialization',
        ),
    ]