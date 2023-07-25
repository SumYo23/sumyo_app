import jwt
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView

from cook.models import Ingredient
from refrigerator.models import Refrigerator
from refrigerator.serializers import RefrigeratorSerializer
from user.models import User


class IngredientList(APIView):
    def get(self, request):

        ''' 토큰 관련 인증 '''
        try:
            token = request.META["HTTP_AUTHORIZATION"]
            payload = jwt.decode(token, 'secretJWTkey', algorithms=['HS256'])
            user_number = payload['user_number']
        except jwt.ExpiredSignatureError:
            response = Response()
            response.data = {
                "message": "토큰 정보가 잘못되었습니다."
            }
            response.status = status.HTTP_400_BAD_REQUEST
            return response

        try:
            user = User.objects.get(user_number=user_number)
            refrigerator = Refrigerator.objects.filter(user__pk=user.pk)

            result = RefrigeratorSerializer(refrigerator).data
            return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)

        except jwt.ExpiredSignatureError:
            response = Response()
            response.data = {
                "message": "데이터 저장 문제가 생겼습니다."
            }
            response.status = status.HTTP_400_BAD_REQUEST
            return response

    def post(self, request):
        ''' 토큰 관련 인증 '''
        try:
            token = request.META["HTTP_AUTHORIZATION"]
            payload = jwt.decode(token, 'secretJWTkey', algorithms=['HS256'])
            user_number = payload['user_number']
        except jwt.ExpiredSignatureError:
            response = Response()
            response.data = {
                "message": "토큰 정보가 잘못되었습니다."
            }
            response.status = status.HTTP_400_BAD_REQUEST
            return response

        try:
            ingredient = request.data["ingredient"]
            quantity = request.data["quantity"]
            user = User.objects.get(user_number=user_number)
            ingredient, _ = Ingredient.objects.get_or_create(name=ingredient)
            refrigerator = Refrigerator.objects.create(ingredient=ingredient, quantity=quantity, user=user)
            refrigerator.save()

            response = Response()
            response.data = {
                "ingredient": refrigerator.ingredient.name,
                "quantity": refrigerator.quantity,
                "date": refrigerator.add_date
            }
            ingredient.save()
            refrigerator.save()

            response.status = status.HTTP_200_OK
            return response

        except jwt.ExpiredSignatureError:
            response = Response()
            response.data = {
                "message": "데이터 저장 문제가 생겼습니다."
            }
            response.status = status.HTTP_400_BAD_REQUEST
            return response
