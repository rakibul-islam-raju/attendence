from django.shortcuts import render, redirect
from datetime import date
from django.contrib import messages
from django.views.generic.edit import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import AttendanceForm
from .models import Attendance


class AttendanceView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        user = self.request.user
        today = date.today()
        attendance_date = Attendance.objects.filter(created_at=today, student=user)
        form = AttendanceForm()
        context = {
            'form': form,
            'attendance_date': attendance_date
        }
        return render(self.request, 'core/attendance.html', context)

    def post(self, *args, **kwargs):
        form = AttendanceForm(self.request.POST or None)
        if form.is_valid():
            present = form.cleaned_data.get('present')
            student = self.request.user
            Attendance.objects.create(
                student=student,
                present=present
            )
            messages.success(self.request, 'Attendance Submitted')
            return redirect('/')
        context = {
            'form': form,
        }
        return render(self.request, 'core/attendance.html', context)
