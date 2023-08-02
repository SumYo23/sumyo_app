from rest_framework import serializers

from refrigerator.models import Refrigerator


class RefrigeratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refrigerator
        fields = ('quantity', "user", "ingredient")
