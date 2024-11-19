from django.urls import path
from .views import GradeView, UpdateGradeView

urlpatterns = [
    path('', GradeView.as_view(), name='grade-list'),
    path('<int:pk>/', UpdateGradeView.as_view(), name='grade-update'),
]
