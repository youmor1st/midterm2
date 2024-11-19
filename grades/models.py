from django.db import models
from students.models import Student
from courses.models import Course
from users.models import User

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    grade = models.CharField(max_length=5)
    date = models.DateField(auto_now_add=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'}, related_name='grades')

    def __str__(self):
        return f"Grade for {self.student.first_name} {self.student.last_name} in {self.course.name}: {self.grade}"
