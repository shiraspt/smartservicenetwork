from django.db import models
from Admin_.models import Location
# Create your models here.
class Employee(models.Model):
    Emp_name = models.CharField(max_length = 50)
    Emp_phone = models.CharField(max_length = 50)
    Emp_email = models.CharField(max_length = 50)
    Emp_Address = models.CharField(max_length = 500)
    Emp_gender = models.CharField(max_length = 50)
    Emp_dob = models.DateField()
    Emp_age=models.IntegerField()
    Emp_location = models.CharField(max_length = 50)
    Emp_photo =  models.ImageField(upload_to='employee/')
    Emp_password = models.CharField(max_length = 50)
    location = models.ForeignKey(Location,on_delete = models.CASCADE, default='')

    class Meta:
        db_table = 'employee_tb'