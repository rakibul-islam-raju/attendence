from django.contrib import admin
from .models import *


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'present', 'created_at', 'updated_at']    
