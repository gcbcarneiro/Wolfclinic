from django.db import models
from phone_field import PhoneField
from django.utils.text import slugify
from django.urls import reverse
    

# Create your models here.

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=30)
    doctor_last_name = models.CharField(max_length=30)
    address = models.TextField()
    phone_number = PhoneField(blank=True)
    salary = models.FloatField()
    TURN = (('1th','1th Turn'),('2nd','2nd Turn'),('3rd','3rd Turn'))
    turn = models.CharField(max_length=3,choices = TURN,default="1th")
    doctor_url = models.SlugField(max_length=60, unique=True)
    MEDICAL_ESPECIALITY = (("Allergology","Allergology"),
                                            ("Anesthesiology","Anesthesiology"),
                                            ("Angiology","Angiology"),
                                            ("Cardiology","Cardiology"),
                                            ("Endocrinology","Endocrinology"),
                                            ("Stomatology","Stomatology"),
                                            ("Gastroenterology","Gastroenterology"),
                                            ("Geriatrics","Geriatrics"),
                                            ("Hematology","Hematology"),
                                            ("Hepatology","Hepatology"),
                                            ("Infectology","Infectology"),
                                            ("Aerospace medicine","Aerospace medicine"),
                                            ("Sports medicine","Sports medicine"),
                                            ("Emergency medicine","Emergency medicine"),
                                            ("Family and community medicine","Family and community medicine"),
                                            ("Physical medicine and rehabilitation","Physical medicine and rehabilitation"),
                                            ("Forensic Medicine","Forensic Medicine"),
                                            ("Intensive medicine","Intensive medicine"),
                                            ("Internal Medicine","Internal Medicine"),
                                            ("preventive medicine and public health","preventive medicine and public health"),
                                            ("Work Medicine","Work Medicine"),
                                            ("Nephrology","Nephrology"),
                                            ("Pneumology","Pneumology"),
                                            ("Neurology","Neurology"),
                                            ("Nutriology","Nutriology"),
                                            ("Medical oncology","Medical oncology"),
                                            ("Radiation Oncology","Radiation Oncology"),
                                            ("Pediatrics","Pediatrics"),
                                            ("Psychiatry","Psychiatry"),
                                            ("Rheumatology","Rheumatology"),
                                            ("Toxicology","Toxicology"))
    medical_speciality = models.CharField(max_length=40,choices = MEDICAL_ESPECIALITY,default="ALL")

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self):
        return self.doctor_name

    def save(self, *args, **kwargs):
        """
        create a url in base to the name and the last name 
        of the doctor
        """
        
        self.doctor_url = slugify(self.doctor_name + '-' + self.doctor_last_name)
        super(Doctor,self).save(*args, **kwargs)

    

class Floor(models.Model):
    FLOOR_NAME = (("Allergology","Allergology"),
                                            ("Anesthesiology","Anesthesiology"),
                                            ("Angiology","Angiology"),
                                            ("Cardiology","Cardiology"),
                                            ("Endocrinology","Endocrinology"),
                                            ("Stomatology","Stomatology"),
                                            ("Gastroenterology","Gastroenterology"),
                                            ("Geriatrics","Geriatrics"),
                                            ("Hematology","Hematology"),
                                            ("Hepatology","Hepatology"),
                                            ("Infectology","Infectology"),
                                            ("Aerospace medicine","Aerospace medicine"),
                                            ("Sports medicine","Sports medicine"),
                                            ("Emergency medicine","Emergency medicine"),
                                            ("Family and community medicine","Family and community medicine"),
                                            ("Physical medicine and rehabilitation","Physical medicine and rehabilitation"),
                                            ("Forensic Medicine","Forensic Medicine"),
                                            ("Intensive medicine","Intensive medicine"),
                                            ("Internal Medicine","Internal Medicine"),
                                            ("preventive medicine and public health","preventive medicine and public health"),
                                            ("Work Medicine","Work Medicine"),
                                            ("Nephrology","Nephrology"),
                                            ("Pneumology","Pneumology"),
                                            ("Neurology","Neurology"),
                                            ("Nutriology","Nutriology"),
                                            ("Medical oncology","Medical oncology"),
                                            ("Radiation Oncology","Radiation Oncology"),
                                            ("Pediatrics","Pediatrics"),
                                            ("Psychiatry","Psychiatry"),
                                            ("Rheumatology","Rheumatology"),
                                            ("Toxicology","Toxicology"))
    floor_name = models.CharField(max_length=40,choices = FLOOR_NAME,default="ALL")
    bed_number = models.IntegerField()
    url = models.SlugField(max_length=255, unique=True)



    class Meta:
        verbose_name = "Floor"
        verbose_name_plural = "Floors"

    def __str__(self):
        return self.floor_name

    def save(self, *args, **kwargs):
        """
        create a url in base to the floor name
        """
        
        self.url = slugify(self.floor_name)
        super(Floor,self).save(*args, **kwargs)
    


class Patient(models.Model):
    patient_name = models.CharField(max_length=30)
    patient_last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    BLOOD_TYPE = ((('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-'),('O+','O+'),('O-','O-')))
    blood_type = models.CharField(max_length=3,choices = BLOOD_TYPE,default="A+")
    address = models.TextField()
    phone_number = PhoneField(blank=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    sickness = models.CharField(max_length=50)
    floor = models.ForeignKey(Floor,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    pacient_url = models.SlugField(max_length=60, unique=True)
    

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def __str__(self):
        return self.patient_name

    def save(self, *args, **kwargs):
        """
        create a url in base to the name and the last name 
        of the patient
        """

        self.pacient_url = slugify(self.patient_name + '-' + self.patient_last_name)
        super(Patient,self).save(*args, **kwargs)




