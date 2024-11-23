from rest_framework import serializers

from core.models import Human


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = (
            'id',
            'first_name',
            'last_name',
            'gender',
            'father',
            'mother',
        )
