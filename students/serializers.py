from rest_framework import serializers
from .models import Student
from courses.models import Course
from grades.models import Grade
from attendance.models import Attendance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description']

class GradeSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Grade
        fields = ['id', 'course', 'grade', 'date', 'teacher']

class AttendanceSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Attendance
        fields = ['id', 'course', 'date', 'status']

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    grades = GradeSerializer(many=True)
    attendance_records = AttendanceSerializer(many=True)
    courses = CourseSerializer(many=True)

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'dob', 'registration_date', 'address', 'phone_number', 'grades', 'attendance_records', 'courses']
