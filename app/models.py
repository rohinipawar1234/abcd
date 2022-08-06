from django.db import models

# Create your models here.
class Employee(models.Model):
    First_name=models.CharField(max_length=50)
    Middle_name=models.CharField(max_length=40)
    Last_name=models.CharField(max_length=30)
    Department=models.CharField(max_length=50,null=True)
    Age=models.IntegerField()
    Mob_no=models.IntegerField()
    Emp_id=models.IntegerField()
    ch_choice=(
        ('Assistent','Assistent'),
        ('Developer','Developer'),
        ('CEO','CEO'),
        ('Manager','Manager'),
    )
    position=models.CharField(max_length=20,choices=ch_choice)
    Email_id=models.EmailField(max_length=30)
    current_address=models.CharField(max_length=20)

    def __str__(self):
        return str(self.Emp_id)


class Salary(models.Model):
    Employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    salary=models.IntegerField()

    def __str__(self):
        return str(self.Employee_id)        