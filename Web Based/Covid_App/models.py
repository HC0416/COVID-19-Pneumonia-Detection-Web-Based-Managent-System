from django.db import models

# Create your models here.
class Patient(models.Model):
    PatientID = models.CharField(max_length=10, blank=False, null=False)
    PatientName = models.CharField(max_length=50, blank=False, null=False)
    PatientGender = models.CharField(max_length=2, blank=False, null=False)
    PatientAge = models.IntegerField()
    PatientPhone = models.CharField(max_length=15, blank=False, null=False)
    Patient_X_Ray_Heatmap = models.FileField()
    PatientPredictedLabel = models.CharField(max_length=10)
    PatientRemark = models.CharField(max_length=100)
    PatientStatus = models.CharField(max_length=20)