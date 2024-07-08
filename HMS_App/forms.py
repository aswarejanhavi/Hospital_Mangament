# patients/forms.py
from django import forms
from .models import Inpatient, Outpatient

class InpatientForm(forms.ModelForm):
    class Meta:
        model = Inpatient
        fields = ['P_ID', 'P_Name', 'P_Age', 'room_number', 'admission_date']

class OutpatientForm(forms.ModelForm):
    class Meta:
        model = Outpatient
        fields = ['P_ID', 'P_Name', 'P_Age', 'appointment_date']
