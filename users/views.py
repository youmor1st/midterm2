from rest_framework import viewsets
from rest_framework.response import Response
from students.models import Student
from students.serializers import StudentSerializer
from users.permissions import IsAdmin, IsTeacher, IsStudent
from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer, UserCreateSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAdmin | IsTeacher]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permission_classes = [IsStudent | IsTeacher | IsAdmin]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        user = User.objects.get(username=request.data['username'])
        token = RefreshToken.for_user(user)
        return Response({'access_token': str(token.access_token), 'refresh_token': str(token)})