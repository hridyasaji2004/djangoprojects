from django.db import models
from django.forms import CharField


class Employee(models.Model):
    emp_id=models.CharField(max_length=30)
    emp_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number=models.CharField(max_length=20)
    designation=models.CharField(max_length=50)
    salary=models.IntegerField()
    image=models.ImageField(upload_to="employees")








