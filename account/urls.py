from django.urls import path, include
from .views import RegisterView, AdminUserCreateAPIView, UserProfile


from django.urls import path
from auth.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    # path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('create-admin/', AdminUserCreateAPIView.as_view()),
    path('profile/<int:pk>/', UserProfile.as_view(), name='profile'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]