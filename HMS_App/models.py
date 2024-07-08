# from django.db import models

# # Create your models here.

# class Doctor(models.Model):
#     Dr_Name=models.CharField(max_length=200)
#     Dr_Degree=models.CharField(max_length=150)   
#     Dr_Specilization=models.CharField(max_length=200)


# class Patient(models.Model):
#     P_ID = models.CharField(max_length=100, unique=True)
#     P_Name = models.CharField(max_length=100)
#     P_Age = models.IntegerField()

#     def __str__(self):
#         return self.P_Name

# class Inpatient(Patient):
#     room_number = models.IntegerField()
#     admission_date = models.DateField()

# class Outpatient(Patient):
#     appointment_date = models.DateField()


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# models.py

from django.db import models

class Doctor(models.Model):
    Dr_Name = models.CharField(max_length=200)
    Dr_Degree = models.CharField(max_length=150)
    Dr_Specialization = models.CharField(max_length=200)

    def __str__(self):
        return self.Dr_Name

class Patient(models.Model):
    P_ID = models.CharField(max_length=100, unique=True)
    P_Name = models.CharField(max_length=100)
    P_Age = models.IntegerField()

    def __str__(self):
        return self.P_Name

class Inpatient(Patient):
    room_number = models.IntegerField()
    admission_date = models.DateField()

class Outpatient(Patient):
    appointment_date = models.DateField()
