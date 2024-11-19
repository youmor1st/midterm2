from django.db import models

from students.models import Student
from users.models import User

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'}, related_name='courses')

    def __str__(self):
        return self.name

class Enrollment(models.Model):
        student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
        course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
        enrollment_date = models.DateField(auto_now_add=True)

        class Meta:
            unique_together = ('student', 'course')

        def __str__(self):
            return f"{self.student.first_name} {self.student.last_name} enrolled in {self.course.name}"