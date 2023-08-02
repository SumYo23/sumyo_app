"""django"""
from django.db import models


# 냉장고
class Refrigerator(models.Model):
    quantity = models.IntegerField(default=0)
    add_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("cook.Ingredient", on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.ingredient.name + " : " + str(self.quantity) + "개"

    class Meta:
        db_table = "sumyo_refrigerator"
        verbose_name = "냉장고"
        verbose_name_plural = "냉장고"
