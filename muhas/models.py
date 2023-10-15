from django.db import models

# Create your models here.

class StudentPassport(models.Model):
    student_name = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    registration_number = models.IntegerField()
    expire_date = models.DateTimeField(auto_now=False, auto_now_add=False)  
    student_pic = models.ImageField(upload_to='passport', height_field=None, width_field=None, max_length=None)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)