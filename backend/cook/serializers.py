from rest_framework import serializers

from cook.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField()
    detail = serializers.CharField(max_length=1000)
    image_route = serializers.CharField(max_length=1000)

    class Meta:
        model = Recipe
        fields = "__all__"
