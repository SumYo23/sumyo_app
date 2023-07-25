from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView

from cook.models import Ingredient
from refrigerator.models import Refrigerator
from refrigerator.serializers import RefrigeratorSerializer
from user.models import User


class RefrigeratorList(APIView):
    def get(self, request):
        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])
        refrigerator = Refrigerator.objects.filter(user__pk=user.pk)

        response = Response()
        response.data = list()
        for refr in refrigerator:
            response.data.append(
                {"ingredient": refr.ingredient.name, "quantity": str(refr.quantity), "date": refr.add_date})
        response.status = status.HTTP_200_OK
        return response

    def post(self, request):
        ingredient = request.data["ingredient"]
        quantity = request.data["quantity"]

        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])
        ingredient_instance, _ = Ingredient.objects.get_or_create(name=ingredient)
        refrigerator_instance, _ = Refrigerator.objects.get_or_create(ingredient=ingredient_instance, user=user)
        refrigerator_instance.quantity = int(refrigerator_instance.quantity) + int(quantity)
        refrigerator_instance.save()

        response = Response()
        response.data = {
            "ingredient": refrigerator_instance.ingredient.name,
            "quantity": refrigerator_instance.quantity,
            "date": refrigerator_instance.add_date
        }
        ingredient_instance.save()
        refrigerator_instance.save()

        response.status = status.HTTP_200_OK
        return response


class RefrigeratorPut(APIView):
    def put(self, request, ingredient, quantity):
        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])
        ingredient_instance = Ingredient.objects.get(name=ingredient)
        refrigerator_instance = Refrigerator.objects.get(ingredient=ingredient_instance, user=user)
        refrigerator_instance.quantity = quantity
        refrigerator_instance.save()
        return Response({"ingredient": refrigerator_instance.ingredient.name, "quantity": quantity,
                         "date": refrigerator_instance.add_date}, status=status.HTTP_201_CREATED)


class RefrigeratorDelete(APIView):
    def delete(self, request, ingredient):
        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])
        ingredient_instance = Ingredient.objects.get(name=ingredient)
        Refrigerator.objects.get(ingredient=ingredient_instance, user=user).delete()
        return Response(status=status.HTTP_200_OK)
