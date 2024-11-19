import logging
from rest_framework import generics, permissions, pagination, status
from rest_framework.response import Response
from rest_framework.views import APIView
from win32timezone import now
from midterm.settings import CACHE_EXPIRATION
from .serializers import CourseSerializer, EnrollmentSerializer
from .models import Course, Enrollment
from django.core.cache import cache
from users.permissions import IsTeacher



class CourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.LimitOffsetPagination

    def get_queryset(self):
        instructor_filter = self.request.query_params.get('instructor', None)
        cache_key = f'course_list_instructor_{instructor_filter}'

        cached_courses = cache.get(cache_key)
        if cached_courses:
            return cached_courses

        queryset = Course.objects.all()

        if instructor_filter:
            queryset = queryset.filter(instructor__username=instructor_filter)

        cache.set(cache_key, queryset, timeout=CACHE_EXPIRATION)
        return queryset


class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        cache.delete('course_list_instructor_*')
        serializer.save()


class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser | IsTeacher]

    def perform_update(self, serializer):
        cache.delete('course_list_instructor_*')
        serializer.save()


course_logger = logging.getLogger('course_actions')

class CourseEnrollmentView(APIView):
    def post(self, request, course_id):
        student = request.user.student_profile
        course = Course.objects.get(id=course_id)

        enrollment = Enrollment.objects.create(student=student, course=course)
        course_logger.info(f"Student {student.user.username} enrolled in course {course.name} at {now()}")

        return Response({"message": "Enrolled successfully"}, status=status.HTTP_201_CREATED)