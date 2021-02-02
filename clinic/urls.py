"""clinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',FloorList.as_view(),name="home"),
    path('create-floor',FloorCreate.as_view(),name="createFloor"),
    path('detail/<slug:url>/',FloorDetail.as_view(),name="detailFloor"),
    path('edit/<slug:url>/',FloorUpdate.as_view(),name="updateFloor"),
    path('delete/<slug:url>',FloorDelete.as_view(),name="deleteFloor"),
    path('create-doctor',DoctorCreate.as_view(),name="createDoctor"),
    path('doctor/<slug:doctor_url>/',DoctorDetail.as_view(),name="detaildoctor"),
    path('doctor/edit/<slug:doctor_url>/',DoctorUpdate.as_view(),name="updatedoctor"),
    path('doctor/delete/<slug:doctor_url>',DoctorDelete.as_view(),name="deletedoctor"),
    path('create-pacient',PatientCreate.as_view(),name="createPacient"),
    path('patient/<slug:pacient_url>/',PatientDetail.as_view(),name="detailpacient"),
    path('patient/edit/<slug:pacient_url>/',PatientUpdate.as_view(),name="updatepacient"),
    path('patient/delete/<slug:pacient_url>',PatientDelete.as_view(),name="deletepacient"),
]
 