from rest_framework import serializers

from .models import Cook
from .models import Ingredient
from .models import Recipe

# class TrackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Track
#         fields = ['order', 'title', 'duration']
#
# class AlbumSerializer(serializers.ModelSerializer):
#     tracks = TrackSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Album
#         fields = ['album_name', 'artist', 'tracks']



class RecipeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'number',
            'detail',
            'image_route',
        )

class IngredientSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = (
            'name',
        )



class CookListSerializer(serializers.ModelSerializer):
    cook_ingredient = IngredientSerilizer(read_only=True, many=True)
    cook_recipe = RecipeSerilizer(read_only=True, many=True)

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


    # name = models.TextField()
    # method = models.CharField(max_length=20, null=True)
    # image_route = models.TextField(null=True)
    # ingredient = models.TextField(null=True)
    # cook_ingredient = models.ManyToManyField(Ingredient, related_name="cooks", through="CookIngredient")
    # cook_recipe