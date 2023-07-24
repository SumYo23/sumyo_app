from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=256)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "sumyo_ingredient"
        verbose_name = "재료"
        verbose_name_plural = "재료"


class Recipe(models.Model):
    number = models.IntegerField()
    detail = models.TextField()
    image_route = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return str(self.number) + ") " + str(self.detail)

    class Meta:
        db_table = "sumyo_recipe"
        verbose_name = "레시피"
        verbose_name_plural = "레시피"


class Cook(models.Model):
    name = models.TextField()
    method = models.CharField(max_length=20, null=True)
    image_route = models.TextField(null=True)
    ingredient = models.TextField(null=True)
    recipe = models.TextField(null=True)
    cook_ingredient = models.ManyToManyField("Ingredient")
    cook_recipe = models.ManyToManyField("Recipe")

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "sumyo_cook"
        verbose_name = "요리"
        verbose_name_plural = "요리"
