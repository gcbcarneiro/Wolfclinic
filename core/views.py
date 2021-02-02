from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Doctor, Patient, Floor

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

# Classes to list the obj in the database
class FloorList(ListView):
    model = Floor
    template_name = "home.html"


# Classes to Create the obj in the database

class PatientCreate(SuccessMessageMixin, CreateView):
    model = Patient
    form = Patient
    fields = ['patient_name', 'patient_last_name', 'age', 'blood_type','address','phone_number','sickness','floor','doctor']
    success_message = 'Patient register successful'
    template_name = "createpatient.html"

    def get_success_url(self):
        return reverse('home')

class DoctorCreate(SuccessMessageMixin, CreateView):
    model = Doctor
    form = Doctor
    fields = ['doctor_name', 'doctor_last_name', 'salary','address','phone_number','turn','medical_speciality']
    success_message = 'Doctor register successful'
    template_name = "createdoctor.html"

    def get_success_url(self):
        return reverse('home')

class FloorCreate(SuccessMessageMixin, CreateView):
    model = Floor
    form = Floor
    fields = ['floor_name', 'bed_number']
    success_message = 'Floor register successful'
    template_name = "createfloor.html"

    def get_success_url(self):
        return reverse('home')

class PatientDetail(DetailView):
    model = Patient
    template_name = "detailpatient.html"
    slug_field = 'pacient_url'
    slug_url_kwarg = 'pacient_url'
    def get_context_data(self, **kwargs):
        context = super(PatientDetail,self).get_context_data(**kwargs)
        context['object'] = self.object
        context['floor'] = Floor.objects.filter( floor_name = self.object.floor)

        return context

class DoctorDetail(DetailView):
    model = Doctor
    template_name = "detaildoctor.html"
    slug_field = 'doctor_url'
    slug_url_kwarg = 'doctor_url'

    def get_context_data(self, **kwargs):
        context = super(DoctorDetail,self).get_context_data(**kwargs)
        context['object'] = self.object
        context['floor'] = Floor.objects.filter( floor_name = self.object.medical_speciality)
        context['patients'] = Patient.objects.filter( doctor = self.object)

        return context

class FloorDetail(DetailView):
    model = Floor
    template_name = "detailfloor.html"
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_context_data(self, **kwargs):
        context = super(FloorDetail,self).get_context_data(**kwargs)
        context['object'] = self.object
        context['doctors'] = Doctor.objects.filter(medical_speciality = self.object)
        context['patients'] = Patient.objects.filter(floor = self.object)
        return context
        
    

class PatientUpdate(SuccessMessageMixin,UpdateView):
    model = Patient
    form = Patient
    fields = ['patient_name', 'patient_last_name', 'age', 'blood_type','address','phone_number','sickness','floor','doctor']
    template_name = "updatepatient.html"
    success_message = 'Patient update successful'
    slug_field = 'pacient_url'
    slug_url_kwarg = 'pacient_url'

    def get_success_url(self):
        return reverse('home')



class DoctorUpdate(SuccessMessageMixin,UpdateView):
    model = Doctor
    form = Doctor
    fields = ['doctor_name', 'doctor_last_name', 'salary','address','phone_number','turn','medical_speciality']
    template_name = "updatedoctor.html"
    success_message = 'Doctor update successful'
    slug_field = 'doctor_url'
    slug_url_kwarg = 'doctor_url'

    def get_success_url(self):
        return reverse('home')

class FloorUpdate(SuccessMessageMixin,UpdateView):
    model = Floor
    form = Floor
    fields = ['bed_number']
    template_name = "updatefloor.html"
    success_message = 'Floor update successful'
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_success_url(self):
        return reverse('home')

class PatientDelete(SuccessMessageMixin,DeleteView):
    model = Patient
    form = Patient
    fields = "__all__"
    slug_field = 'pacient_url'
    slug_url_kwarg = 'pacient_url'

    def get_success_url(self):
        success_message = 'Patient delete successful'
        messages.success(self.request, (success_message))
        return reverse('home')

class DoctorDelete(SuccessMessageMixin,DeleteView):
    model = Doctor
    form = Doctor
    fields = "__all__"
    slug_field = 'doctor_url'
    slug_url_kwarg = 'doctor_url'

    def get_success_url(self):
        success_message = 'Doctor delete successful'
        messages.success(self.request, (success_message))
        return reverse('home')

class FloorDelete(SuccessMessageMixin,DeleteView):
    model = Floor
    form = Floor
    fields = "__all__"
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_success_url(self):
        success_message = 'Floor delete successful'
        messages.success(self.request, (success_message))
        return reverse('home')



    