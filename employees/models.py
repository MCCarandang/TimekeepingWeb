from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    rfid_card = models.CharField(max_length=50, unique=True, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Resigned', 'Resigned'), ('Terminated', 'Terminated')])

    def __str__(self):
        return self.name
