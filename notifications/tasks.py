from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime
from django.contrib.auth.models import User

@shared_task
def send_daily_attendance_reminder():
    students = User.objects.filter(role='student')
    for student in students:
        send_mail(
            'Daily Attendance Reminder',
            'Please mark your attendance for today.',
            'from@example.com',
            [student.email],
            fail_silently=False,
        )
    return 'Daily Attendance Reminder Sent'

@shared_task
def send_grade_update_notification(student_id, grade):
    student = User.objects.get(id=student_id)
    send_mail(
        'Grade Update Notification',
        f'Your grade has been updated to {grade}.',
        'from@example.com',
        [student.email],
        fail_silently=False,
    )
    return f'Grade Update Notification Sent to {student.email}'

@shared_task
def send_weekly_performance_report():
    students = User.objects.filter(role='student')
    for student in students:

        performance_report = f"Weekly Report for {student.username}: [Insert performance data here]"
        send_mail(
            'Weekly Performance Report',
            performance_report,
            'from@example.com',
            [student.email],
            fail_silently=False,
        )
    return 'Weekly Performance Report Sent'
