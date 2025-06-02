from rest_framework import serializers
from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        extra_kwargs = {
            'code': {
                'error_messages': {
                    'blank': 'Subject code cannot be blank',
                    'max_length': 'Subject code cannot be longer than 20 characters',
                    'unique': 'This subject code already exists'
                }
            },
            'name': {
                'error_messages': {
                    'blank': 'Subject name cannot be blank',
                    'max_length': 'Subject name cannot be longer than 100 characters'
                }
            },
            'credits': {
                'error_messages': {
                    'invalid': 'Credits must be a positive integer'
                }
            },
            'description': {
                'required': False,  # Make description optional
                'allow_blank': True,
                'allow_null': True
            }
        }

    def validate_code(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Subject code can only contain letters and numbers")
        return value.upper()  # Convert to uppercase for consistency

    def validate_credits(self, value):
        if value < 1:
            raise serializers.ValidationError("Credits must be at least 1")
        return value