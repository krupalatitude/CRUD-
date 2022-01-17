from django.db import models

# Create your models here.

class EmployeeData(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_address = models.CharField(max_length=200)
    emp_salary = models.IntegerField(default=0)
    

    def __str__(self):
        return self.emp_name
