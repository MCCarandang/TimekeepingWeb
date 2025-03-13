from django.db import models
from employees.models import Employee

class AttendanceLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[("IN", "Clock In"), ("OUT", "Clock Out")])

    def __str__(self):
        return f"{self.employee.name} - {self.timestamp} ({self.status})"
