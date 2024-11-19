from django.template.defaulttags import now
from rest_framework import generics, permissions
from courses.models import Course
from students.models import Student
from .serializers import AttendanceSerializer
from .models import Attendance
from users.permissions import IsTeacher
from rest_framework.views import APIView
from rest_framework.response import Response
import logging

class AttendanceView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

class AttendanceUpdateView(generics.UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsTeacher]

attendance_logger = logging.getLogger('attendance_actions')

class MarkAttendanceView(APIView):
    def post(self, request, student_id, course_id):
        student = Student.objects.get(id=student_id)
        course = Course.objects.get(id=course_id)
        status = request.data.get('status')

        attendance_record, created = Attendance.objects.update_or_create(
            student=student, course=course, defaults={'status': status}
        )

        # Log the attendance action
        attendance_logger.info(f"Attendance marked for student {student.user.username} in course {course.name} as {status} at {now()}")

        return Response({"message": "Attendance marked successfully"}, status=status.HTTP_200_OK)
