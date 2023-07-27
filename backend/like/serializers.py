from rest_framework import serializers

from .models import Like
from rest_framework import serializers

from .models import Like
from cook.models import Recipe
from cook.models import Ingredient
from cook.models import Cook

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


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

class LikeListSerializer(serializers.ModelSerializer):
    cook = CookListSerializer(read_only=True)

    class Meta:
        model = Like
        fields = [
            'cook',
            'user',
        ]

