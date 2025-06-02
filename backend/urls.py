from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from students import views as student_views
from subjects import views as subject_views
from grades import views as grade_views

router = routers.DefaultRouter()
router.register(r'students', student_views.StudentViewSet)
router.register(r'subjects', subject_views.SubjectViewSet)
router.register(r'grades', grade_views.GradeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  
    path('', include('frontend.urls')),  
]
