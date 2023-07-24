from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_number',)

    def create(self, validated_data):
        user = User.objects.create_user(
            user_number=validated_data['user_number']
        )
        return user
#
