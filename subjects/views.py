# subjects/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Subject
from .serializers import SubjectSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all().order_by('code')
    serializer_class = SubjectSerializer

def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    logger.error(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            subject = self.get_object()
            serializer = self.get_serializer(subject)
            return Response(serializer.data)
        except Subject.DoesNotExist:
            return Response(
                {'error': 'Subject not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk=None):
        try:
            subject = self.get_object()
            serializer = self.get_serializer(subject, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Subject.DoesNotExist:
            return Response(
                {'error': 'Subject not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )

    def destroy(self, request, pk=None):
        try:
            subject = self.get_object()
            subject.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Subject.DoesNotExist:
            return Response(
                {'error': 'Subject not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )