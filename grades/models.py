# grades/models.py

from django.db import models
from students.models import Student
from subjects.models import Subject
from decimal import Decimal

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    activity_grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    quiz_grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    exam_grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.subject}"

    def final_grade(self):
        # Define the weights for each component
        activity_weight = Decimal('0.20')
        quiz_weight = Decimal('0.30')
        exam_weight = Decimal('0.50')

        # Calculate the percentage for each component
        activity_percentage = (self.activity_grade / Decimal('100')) * Decimal('100') if self.activity_grade is not None else Decimal('0')
        quiz_percentage = (self.quiz_grade / Decimal('100')) * Decimal('100') if self.quiz_grade is not None else Decimal('0')
        exam_percentage = (self.exam_grade / Decimal('100')) * Decimal('100') if self.exam_grade is not None else Decimal('0')

        # Apply the weights to each component
        activity_weighted = activity_percentage * activity_weight
        quiz_weighted = quiz_percentage * quiz_weight
        exam_weighted = exam_percentage * exam_weight

        # Calculate the final grade by summing the weighted percentages
        final_grade = activity_weighted + quiz_weighted + exam_weighted

        return final_grade