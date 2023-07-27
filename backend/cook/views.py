'''builtin'''
from collections import Counter
import random

'''Third-Party'''
from rest_framework.response import Response
from rest_framework.views import APIView
'''local'''
from user.models import User
from refrigerator.models import Refrigerator
from cook.models import Cook, CookIngredient, CookRecipe, Ingredient
from like.models import Like


# [GET] 0.0.0.0/api/cook/list/
class CookList(APIView):
    """사용자별 음식 추천 목록 보여주기"""

    def get(self, request, num):
        # 사용자 정보
        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])

        # 냉장고 재고
        user_ingredient = Refrigerator.objects.filter(user=user).values_list("ingredient", flat=True)

        # 냉장고 재고와 겹치는 요리들 일치율 순서로 정렬
        user_cook = CookIngredient.objects.filter(ingredient__in=user_ingredient).values_list("cook", flat=True)
        user_cook_cnt = Counter(list(user_cook))
        for k, v in user_cook_cnt.items():
            user_cook_cnt[k] = int(v / CookIngredient.objects.filter(cook__pk=int(k)).count() * 100)
        user_cook_cnt = user_cook_cnt
        user_cook_cnt = sorted(user_cook_cnt.items(), key=lambda x: x[1], reverse=True)  # 겹치는 개수 순서로 정렬

        # 사용자와 안겹치는 요리 목록
        cook_list = list(set(Cook.objects.all().values_list("pk", flat=True)) - set(user_cook))

        # 요청받은 요리 수만큼 보여줌
        result = list()
        for i in range(num):
            if len(user_cook_cnt) >= i + 1:
                pk = user_cook_cnt[i][0]
                cook = Cook.objects.get(pk=pk)
                percent = user_cook_cnt[i][1]
                status = "추천"
            else:
                pk = cook_list.pop(random.randrange(len(cook_list)))
                cook = Cook.objects.get(pk=pk)
                percent = 0
                status = "랜덤"

            # 요리 순서별로 recipes 변수에 저장
            recipes = list()
            for recipe in CookRecipe.objects.filter(cook__pk=pk):
                recipes.append(
                    {
                        "number": recipe.recipe.number,
                        "detail": recipe.recipe.detail,
                        "image_route": recipe.recipe.image_route
                    }
                )


            # 요리 재료 ingredients 변수에 저장
            ingredients = list()
            for ingredient in CookIngredient.objects.filter(cook__pk=pk):
                ingredients.append(
                    {"name": ingredient.ingredient.name}
                )

            # 결과
            result.append(
                {
                    "id": cook.pk,
                    "image_route": cook.image_route,
                    "name": cook.name,
                    "percent": percent,
                    "status": status,
                    "ingredient": cook.ingredient.replace('주재료', '').split(','),
                    "recipes": recipes,
                    "ingredients": ingredients

                }
            )

        response = Response()
        response.data = result
        return response


class IngredientList(APIView):
    """db 전체 재료(ingredient) 리스트 반환"""
    def get(self, request):
        ingredient_list = list(Ingredient.objects.all().values_list("name", flat=True))
        return Response(ingredient_list)
