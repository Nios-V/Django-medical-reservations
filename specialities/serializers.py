from rest_framework import serializers
from .models import Speciality


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
