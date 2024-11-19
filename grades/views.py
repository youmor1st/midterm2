import logging
from django.template.defaulttags import now
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from courses.models import Course
from students.models import Student
from .serializers import GradeSerializer
from .models import Grade
from users.permissions import IsTeacher

class GradeView(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticated]

grade_logger = logging.getLogger('grade_actions')

class UpdateGradeView(APIView):
    def post(self, request, student_id, course_id):
        student = Student.objects.get(id=student_id)
        course = Course.objects.get(id=course_id)
        grade = request.data.get('grade')

        grade_record, created = Grade.objects.update_or_create(
            student=student, course=course, defaults={'grade': grade}
        )

        # Log the grade update action
        grade_logger.info(f"Grade updated for student {student.user.username} in course {course.name} to {grade} at {now()}")

        return Response({"message": "Grade updated successfully"}, status=status.HTTP_200_OK)
