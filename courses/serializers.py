from rest_framework import serializers
from .models import Course, Enrollment
from students.models import Student

class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.StringRelatedField()

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'instructor', 'created_at', 'updated_at']

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    course = CourseSerializer()

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrollment_date']
