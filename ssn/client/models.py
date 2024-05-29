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