from django.db import models

# Create your models here.
from backend.user.models import User


class Refrigerator(models.Model):
    count = models.IntegerField()
    add_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("Ingredient", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user_number + " => " + self.ingredient.name + " : " + self.count + "개"

    class Meta:
        db_table = "sumyo_refrigerator"
        verbose_name = "냉장고"
        verbose_name_plural = "냉장고"