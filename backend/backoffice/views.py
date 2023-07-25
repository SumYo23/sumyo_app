import os

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

from cook.models import Cook, Recipe, Ingredient


def import_csv(request):
    if request.method == "POST" and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        csv_file = uploaded_file_url
        raw_data = pd.read_csv("." + csv_file, encoding='cp949')
        os.remove("." + csv_file)
        raw_data = raw_data.filter(
            ['name', 'method', 'image_route', 'ingredient', 'recipe_1', 'recipe_image_1', 'recipe_2',
             'recipe_image_2', 'recipe_3', 'recipe_image_3', 'recipe_4', 'recipe_image_4', 'recipe_5', 'recipe_image_5',
             'recipe_6', 'recipe_image_6', 'cook_ingredient'])
        raw_data = raw_data.fillna("")

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
