# from django.shortcuts import render

# # Create your views here.
# # patients/views.py
# # myapp/views.py

# from django.views.generic import ListView, DetailView
# from .models import Doctor, Inpatient, Outpatient

# class DoctorListView(ListView):
#     model = Doctor
#     template_name = 'doctor_list.html'
#     context_object_name = 'doctors'

# class DoctorDetailView(DetailView):
#     model = Doctor
#     template_name = 'doctor_detail.html'
#     context_object_name = 'doctor'

# class InpatientListView(ListView):
#     model = Inpatient
#     template_name = 'inpatient_list.html'
#     context_object_name = 'inpatients'

# class InpatientDetailView(DetailView):
#     model = Inpatient
#     template_name = 'inpatient_detail.html'
#     context_object_name = 'inpatient'

# class OutpatientListView(ListView):
#     model = Outpatient
#     template_name = 'outpatient_list.html'
#     context_object_name = 'outpatients'

# class OutpatientDetailView(DetailView):
#     model = Outpatient
#     template_name = 'outpatient_detail.html'
#     context_object_name = 'outpatient'


# def index(request):
#     return render(request, 'index.html')
# def doctor_list(request):
#     return render(request, 'doctor_list.html')
# def patient_list(request):
#     return render(request,'patient_list')
# def inpatient_list(request):
#     return render(request,'inpatient_list')
# def outpatient_list(request):
#     return render(request,'outpatient_list')
# def doctor_detail(request):
#     return render(request,'doctor_detail')
# def patient_detail(request):
#     return render(request,'patient_detail')

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# views.py

from django.views.generic import ListView, DetailView
from .models import Doctor, Inpatient, Outpatient

class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor_list.html'
    context_object_name = 'doctors'

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctor_detail.html'
    context_object_name = 'doctor'

class InpatientListView(ListView):
    model = Inpatient
    template_name = 'inpatient_list.html'
    context_object_name = 'inpatients'

class InpatientDetailView(DetailView):
    model = Inpatient
    template_name = 'inpatient_detail.html'
    context_object_name = 'inpatient'

class OutpatientListView(ListView):
    model = Outpatient
    template_name = 'outpatient_list.html'
    context_object_name = 'outpatients'

class OutpatientDetailView(DetailView):
    model = Outpatient
    template_name = 'outpatient_detail.html'
    context_object_name = 'outpatient'

