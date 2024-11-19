from django.db import models
from students.models import Student
from courses.models import Course

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])

    def __str__(self):
        return f"Attendance for {self.student.first_name} {self.student.last_name} in {self.course.name} on {self.date}: {self.status}"
