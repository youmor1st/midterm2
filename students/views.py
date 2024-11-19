from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsTeacher
from midterm.settings import CACHE_EXPIRATION
from .models import Student
from .serializers import StudentSerializer
from users.permissions import IsStudent, IsTeacher, IsAdmin
from rest_framework import generics, permissions
from django.core.cache import cache


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update']:
            return [IsAuthenticated(), IsStudent()]
        elif self.action in ['create', 'destroy']:
            return [IsAuthenticated(), IsTeacher()]
        return [IsAuthenticated(), IsAdmin()]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'student':
            return Student.objects.filter(user=user)
        return Student.objects.all()


class StudentProfileView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        student_profile = self.request.user.student_profile

        cache_key = f'student_profile_{student_profile.id}'
        cached_profile = cache.get(cache_key)

        if cached_profile:
            return cached_profile

        cache.set(cache_key, student_profile, timeout=CACHE_EXPIRATION)
        return student_profile

    def perform_update(self, serializer):
        cache_key = f'student_profile_{self.get_object().id}'
        cache.delete(cache_key)

        super().perform_update(serializer)