"""built-in"""
import os
import pandas as pd

"""django"""
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

"""local"""
from cook.models import Cook, Recipe, Ingredient


def import_csv(request):
    """
    - csv파일을 db에 저장하는 함수
    - 지정된 형시에 맞춘 csv만 넣을 수 있음
    - 'name', 'method', 'image_route', 'ingredient', 'recipe_1', 'recipe_image_1', "...", 'recipe_image_6'
    """

    if request.method == "POST" and request.FILES['myfile']:
        # csv 파일 pandas DataFrame에 저장
        myfile = request.FILES['myfile']
        fs = FileSystemStorage().save(myfile.name, myfile)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        csv_file = uploaded_file_url
        raw_data = pd.read_csv("." + csv_file, encoding='cp949')
        os.remove("." + csv_file)

        # 지정된 형식 저장
        raw_data = raw_data.filter(
            ['name', 'method', 'image_route', 'ingredient', 'recipe_1', 'recipe_image_1', 'recipe_2',
             'recipe_image_2', 'recipe_3', 'recipe_image_3', 'recipe_4', 'recipe_image_4', 'recipe_5', 'recipe_image_5',
             'recipe_6', 'recipe_image_6', 'cook_ingredient'])
        raw_data = raw_data.fillna("")

        # Cook과 연결된 ingredient와 recipe를 저장 - ManyToMany Field를 명시하는 연결테이블을 새로 만들어서, 코드 수정이 필요함
        for index, row in raw_data.iterrows():
            obj = Cook.objects.create(name=row['name'], method=row['method'], image_route=row['image_route'],
                                      ingredient=row['ingredient'])

            if row['cook_ingredient'] != "":
                cook_ingredient = row['cook_ingredient'].split(",")
                for i in cook_ingredient:
                    ingredient, _ = Ingredient.objects.get_or_create(name=i.strip())
                    obj.cook_ingredient.add(ingredient)
                    ingredient.save()
            for i in range(1, 7):
                recipe_i = "recipe_" + str(i)
                recipe_image_i = "recipe_image_" + str(i)
                if row[recipe_i] != "":
                    recipe = Recipe.objects.create(number=i, detail=row[recipe_i], image_route=row[recipe_image_i])
                    obj.cook_recipe.add(recipe)
                    recipe.save()
            obj.save()
    else:
        return render(request, "import_csv.html")
    return HttpResponse("성공")
