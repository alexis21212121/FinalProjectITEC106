# grades/serializers.py

from rest_framework import serializers
from .models import Grade
from students.serializers import StudentSerializer
from students.models import Student
from subjects.serializers import SubjectSerializer
from subjects.models import Subject

class GradeSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='student', write_only=True)
    subject_id = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(), source='subject', write_only=True)
    final_grade = serializers.SerializerMethodField()

    class Meta:
        model = Grade
        fields = '__all__'
        extra_fields = ['final_grade']

    def get_final_grade(self, obj):
        return obj.final_grade()