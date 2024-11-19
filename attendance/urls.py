from django.urls import path
from .views import AttendanceView, AttendanceUpdateView

urlpatterns = [
    path('', AttendanceView.as_view(), name='attendance-list'),
    path('<int:pk>/', AttendanceUpdateView.as_view(), name='attendance-update'),
]
