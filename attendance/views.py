from django.shortcuts import render
from .models import AttendanceLog

def attendance_logs(request):
    logs = AttendanceLog.objects.all()
    return render(request, "attendance/logs.html", {"logs": logs})
