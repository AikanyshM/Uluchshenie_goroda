from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', CategoryModelViewSet, basename="category")
router.register(r'news', NewsViewSet, basename='news')
router.register(r'application', ApplicationViewSet, basename="application")



urlpatterns = [
    path('', include(router.urls)),

]