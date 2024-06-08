from django.db import models

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length = 50)
    client_phone = models.CharField(max_length = 50)
    client_email = models.CharField(max_length = 50)
    client_Address = models.CharField(max_length = 500)
    client_password = models.CharField(max_length = 50)
   

    class Meta:
        db_table = 'client_tb'


class Job_type(models.Model):
    job_name = models.CharField(max_length = 50)
class Meta:
    db_table = 'jobtype_tb'




class Work(models.Model):
    client_id:models.IntegerField
    client_location = models.CharField(max_length = 50)
    location = models.ForeignKey(Location,on_delete = models.CASCADE)
    date= models.DateField
    worknumber=models.IntegerField
    work_details=models.CharField(max_length = 500)
    status=models.CharField(max_length = 500)
    work_duration=models.IntegerField
    employee_id=models.ForeignKey(Location,on_delete = models.CASCADE)
