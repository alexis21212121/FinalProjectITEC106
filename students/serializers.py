from rest_framework import serializers
from .models import Student
from django.core.validators import EmailValidator

class StudentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[EmailValidator(message="Enter a valid email address")]
    )
    
    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {
            'student_id': {
                'error_messages': {
                    'blank': 'Student ID cannot be blank',
                    'unique': 'This student ID already exists'
                }
            },
            'date_of_birth': {
                'error_messages': {
                    'invalid': 'Enter a valid date in YYYY-MM-DD format'
                }
            }
        }

    def validate(self, data):
        errors = {}
        if len(data.get('first_name', '')) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        
        if errors:
            raise serializers.ValidationError(errors)
        return data