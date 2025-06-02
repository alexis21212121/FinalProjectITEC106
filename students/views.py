# students/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import action

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('last_name')
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            student = self.get_object()
            serializer = self.get_serializer(student)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response(
                {'error': 'Student not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk=None):
        try:
            student = self.get_object()
            serializer = self.get_serializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response(
                {'error': 'Student not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )

    def destroy(self, request, pk=None):
        try:
            student = self.get_object()
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response(
                {'error': 'Student not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=['get'])
    def grades(self, request, pk=None):
        student = self.get_object()
        grades = student.grade_set.all()
        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)