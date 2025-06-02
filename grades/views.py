# grades/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Grade
from .serializers import GradeSerializer
from students.models import Student
from subjects.models import Subject
from decimal import Decimal

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                student = Student.objects.get(pk=request.data.get('student_id'))
                subject = Subject.objects.get(pk=request.data.get('subject_id'))
            except (Student.DoesNotExist, Subject.DoesNotExist) as e:
                return Response(
                    {'error': str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            if Grade.objects.filter(student=student, subject=subject).exists():
                return Response(
                    {'error': 'Grade record already exists for this student and subject'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            grade = serializer.save(student=student, subject=subject)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        grade = self.get_object()
        serializer = self.get_serializer(grade, data=request.data, partial=True)
        if serializer.is_valid():
            grade_data = request.data
            for grade_type in ['activity_grade', 'quiz_grade', 'exam_grade']:
                if grade_type in grade_data:
                    grade_value = grade_data[grade_type]
                    if grade_value is not None and (Decimal(str(grade_value)) < 0 or Decimal(str(grade_value)) > 100):
                        return Response(
                            {'error': f'{grade_type} must be between 0 and 100'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            grade = self.get_object()
            grade.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Grade.DoesNotExist:
            return Response(
                {'error': 'Grade not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )