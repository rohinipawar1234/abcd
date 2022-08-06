from django.contrib import admin
from .models import Employee,Salary

class Emp_data(admin.ModelAdmin):
    List_display=('First_name','Last_name','Middle_name','Department','Age','Mob_no','Emp_id')

# Register your models here.
admin.site.register(Employee,Emp_data)
admin.site.register(Salary)

