from django.urls import path, include
from .views import UserCreateView, UserLoginView


urlpatterns = [
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]
