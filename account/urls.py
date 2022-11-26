from django.urls import path, include
from .views import RegisterView, AdminUserCreateAPIView, UserProfile


urlpatterns = [
    # path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('create-admin/', AdminUserCreateAPIView.as_view()),
    path('profile/<int:pk>/', UserProfile.as_view(), name='profile'),
]