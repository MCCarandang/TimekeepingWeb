from django.db import models

class DefectiveRFID(models.Model):
    rfid_card = models.CharField(max_length=50, unique=True)
    employee = models.ForeignKey("employees.Employee", on_delete=models.CASCADE)
    reported_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Replaced", "Replaced")])

    def __str__(self):
        return f"Defective RFID: {self.rfid_card}"
