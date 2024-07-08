# myapp/urls.py

# from django.urls import path
# from . import views



# urlpatterns = [
#     path('doctors/', views.DoctorListView.as_view(), name='doctor-list'),
#     path('doctor/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail'),
#     path('inpatients/', views.InpatientListView.as_view(), name='inpatient-list'),
#     path('inpatient/<int:pk>/', views.InpatientDetailView.as_view(), name='inpatient-detail'),
#     path('outpatients/', views.OutpatientListView.as_view(), name='outpatient-list'),
#     path('outpatient/<int:pk>/', views.OutpatientDetailView.as_view(), name='outpatient-detail'),
# ]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('doctors/', views.doctor_list, name='doctor_list'),
#     path('patients/', views.patient_list, name='patient_list'),
#     path('inpatients/', views.inpatient_list, name='inpatient_list'),
#     path('outpatients/', views.outpatient_list, name='outpatient_list'),
#     path('doctor/<int:id>/', views.doctor_detail, name='doctor_detail'),
#     path('patient/<int:id>/', views.patient_detail, name='patient_detail'),
#     # Add more URL patterns as needed
# ]

# from django.urls import path
# from .views import (
#     DoctorListView, DoctorDetailView, InpatientListView, InpatientDetailView,
#     OutpatientListView, OutpatientDetailView, index, doctor_list, patient_list, 
#     inpatient_list, outpatient_list, doctor_detail, patient_detail
# )

# urlpatterns = [
#     path('', index, name='index'),
#     path('doctors/', DoctorListView.as_view(), name='doctor_list'),
#     path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
#     path('inpatients/', InpatientListView.as_view(), name='inpatient_list'),
#     path('inpatients/<int:pk>/', InpatientDetailView.as_view(), name='inpatient_detail'),
#     path('outpatients/', OutpatientListView.as_view(), name='outpatient_list'),
#     path('outpatients/<int:pk>/', OutpatientDetailView.as_view(), name='outpatient_detail'),
#     path('doctors/list/', doctor_list, name='doctor_list_function'),
#     path('patients/list/', patient_list, name='patient_list_function'),
#     path('inpatients/list/', inpatient_list, name='inpatient_list_function'),
#     path('outpatients/list/', outpatient_list, name='outpatient_list_function'),
#     path('doctors/detail/', doctor_detail, name='doctor_detail_function'),
#     path('patients/detail/', patient_detail, name='patient_detail_function'),
# ]


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# urls.py

from django.urls import path
from .views import (
    DoctorListView, DoctorDetailView, InpatientListView, InpatientDetailView,
    OutpatientListView, OutpatientDetailView
)

urlpatterns = [
    path('HMS_App/', DoctorListView.as_view(), name='doctor_list'),
    path('HMS_App/doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('HMS_App/inpatients/', InpatientListView.as_view(), name='inpatient-list'),
    path('HMS_App/inpatients/<int:pk>/', InpatientDetailView.as_view(), name='inpatient_detail'),
    path('HMS_App/outpatients/', OutpatientListView.as_view(), name='outpatient_list'),
    path('HMS_App/outpatients/<int:pk>/', OutpatientDetailView.as_view(), name='outpatient-detail'),   
    path('doctors/', DoctorListView.as_view(), name='doctor_list'),
    path('inpatients/', InpatientListView.as_view(), name='inpatient_list'),
    path('outpatients/', OutpatientListView.as_view(), name='outpatient_list'),
    
]
