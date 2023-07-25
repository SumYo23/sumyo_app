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
        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])
        refrigerator = Refrigerator.objects.filter(user__pk=user.pk)

        result = RefrigeratorSerializer(refrigerator).data
        return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        ingredient = request.data["ingredient"]
        quantity = request.data["quantity"]
        print(request.META)
        #print(request.META["HTTP_CONTENT-LENGTH"])
        print(request.META["HTTP_HOST"])
        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])
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

