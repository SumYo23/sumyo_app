# from rest_framework import serializers
#
# from user.models import SumyoUser
#
#
# class SumyoUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SumyoUser
#         fields = ('user_number', )
#
#     def create(self, validated_data):
#         sumyo_user = SumyoUser.objects.create_user(
#             user_number=validated_data['user_number']
#         )
#         return sumyo_user
#
