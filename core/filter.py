import django_filters
from .models import Attendance


class AttendanceFilter(django_filters.FilterSet):
    
    class Meta:
        model = Attendance
        fields = {
            'created_at': ['gt', 'lt']
        }
