from rest_framework import serializers

from .models import Cook
from .models import Ingredient
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'number',
            'detail',
            'image_route',
        )


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = (
            'name',
        )


class CookListSerializer(serializers.ModelSerializer):
    cook_ingredient = IngredientSerializer(read_only=True, many=True)
    cook_recipe = RecipeSerializer(read_only=True, many=True)

    class Meta:
        model = Cook
        fields = [
            'name',
            'method',
            'image_route',
            'ingredient',
            'cook_ingredient',
            'cook_recipe',
        ]
