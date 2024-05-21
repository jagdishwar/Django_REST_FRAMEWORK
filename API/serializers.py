from dataclasses import field
from statistics import mode
from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    """
    Allows converting complex data into native Python datatypes.
    """
    class Meta:
        model = Course
        fields = '__all__'