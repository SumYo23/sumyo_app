from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "sumyo_ingredient"
        verbose_name = "재료"
        verbose_name_plural = "재료"


class Recipe(models.Model):
    number = models.IntegerField()
    detail = models.TextField()
    image_route = models.CharField(max_length=256)

    def __str__(self):
        return str(self.number) + ") " + str(self.detail)

    class Meta:
        db_table = "sumyo_recipe"
        verbose_name = "레시피"
        verbose_name_plural = "레시피"


class Cook(models.Model):
    name = models.TextField()
    method = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    ingredient = models.TextField()
    recipe = models.TextField()
    cook_ingredient = models.ManyToManyField("Ingredient")
    cook_recipe = models.ManyToManyField("Recipe")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "sumyo_cook"
        verbose_name = "요리"
        verbose_name_plural = "요리"
