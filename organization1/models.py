from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    dep_name = models.CharField(max_length=50, unique=True)
    dep_code = models.CharField(max_length=10, unique=True)
    dep_isactive = models.CharField(
        choices={"Y": "ACTIVE", "N": "INACTIVE"}, max_length=1
    )
    dep_created_at = models.DateTimeField(auto_now_add=True)
    dep_created_by = models.ForeignKey(User, on_delete=models.PROTECT)


class Employee(models.Model):
    emp_fname = models.CharField(max_length=100, null=False)
    emp_lname = models.CharField(max_length=100, null=False)
    emp_fullname = models.CharField(max_length=100, null=False)
    emp_joined = models.DateTimeField(auto_now_add=True)
    emp_code = models.CharField(primary_key=True, max_length=10)
    emp_department = models.OneToOneField(Department, on_delete=models.PROTECT)
    emp_isactive = models.CharField(
        choices={"Y": "ACTIVE", "N": "INACTIVE"}, max_length=1
    )
    emp_added_by = models.ForeignKey(User, on_delete=models.PROTECT)


class DepartmentTest(models.Model):
    dep_name = models.CharField(max_length=50, unique=True)
    dep_code = models.CharField(max_length=10, unique=True)
    dep_isactive = models.CharField(
        choices={"Y": "ACTIVE", "N": "INACTIVE"}, max_length=1
    )
    dep_created_at = models.DateTimeField(auto_now_add=True)
    dep_created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.dep_name
