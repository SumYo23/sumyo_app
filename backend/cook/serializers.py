from rest_framework import serializers

from cook.models import Recipe


class RecipeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = [
            'number',
            'detail',
            'image_route',
        ]
