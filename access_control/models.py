from django.db import models
from employees.models import Employee

class AccessDeniedLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()

    def __str__(self):
        return f"Access Denied: {self.employee.name} - {self.timestamp}"
