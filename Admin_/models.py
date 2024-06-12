from django.db import models



# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length = 50)
    
    class Meta:
        db_table = 'location_tb'


class Applications(models.Model):
    from client.models import Client,Work
    from employee.models import Employee

    work=models.ForeignKey(Work,on_delete = models.CASCADE, default='')
    worknumber=models.CharField(max_length=10)
    Quoted_amount=(models.FloatField)
    employee= models.ForeignKey(Employee,on_delete = models.CASCADE, default='')
    client= models.ForeignKey(Client,on_delete = models.CASCADE, default='')
    status=models.CharField(max_length=50,default="Waiting")

    class Meta:
        db_table = 'appilications_tb'