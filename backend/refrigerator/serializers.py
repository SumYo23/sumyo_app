from rest_framework import serializers

from .models import Refrigerator


class RefrigeratorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refrigerator
        fields = (
            'quantity',
            'user',
            'ingredient',
        )