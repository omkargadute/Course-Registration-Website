from django.db import models

# Create your models here.
class studentDetails(models.Model):
    stud_fname = models.CharField(max_length=100)
    stud_sname = models.CharField(max_length=100)
    stud_gender = models.CharField(max_length=10)
    stud_email = models.CharField(max_length=100)
    stud_course = models.CharField(max_length=100)