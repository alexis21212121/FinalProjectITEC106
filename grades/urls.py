# grades/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GradeViewSet

# this is our root url file


router = DefaultRouter()
router.register(r'grades', GradeViewSet, basename='grade')

urlpatterns = [
    path('', include(router.urls)),
]
