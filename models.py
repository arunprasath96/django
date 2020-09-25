from django.db import models

# Create your models here.
class EmployeeDetail(models.Model):
	emp_id = models.AutoField(primary_key=True)
	emp_name = models.CharField(max_length=100)
	emp_salary = models.IntegerField()
	emp_desgination = models.CharField(max_length=100)
	emp_city = models.CharField(max_length=100)


	class meta:
		db_table = 'employee'
		verbose_name = 'employee_detail'
