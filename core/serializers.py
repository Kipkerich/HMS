from rest_framework import serializers
from .models import Client, Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    program_name = serializers.CharField(source='program.name')

    class Meta:
        model = Enrollment
        fields = ['program_name', 'date_enrolled']

class ClientSerializer(serializers.ModelSerializer):
    enrolled_programs = EnrollmentSerializer(source='enrollment_set', many=True)

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'dob', 'contact', 'enrolled_programs']
