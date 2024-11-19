from django.urls import path
from .views import CourseListView, CourseCreateView, CourseEnrollmentView,CourseUpdateView

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('enroll/', CourseEnrollmentView.as_view(), name='course-enroll'),
    path('update/', CourseUpdateView.as_view(), name='course-update'),

]
