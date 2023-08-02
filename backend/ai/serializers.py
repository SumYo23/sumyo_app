'''Third-Party'''
from rest_framework import serializers
'''Local'''
from ai.models import Image


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = "__all__"
