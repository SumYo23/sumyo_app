from django.db import models

# Create your models here.


class Refrigerator(models.Model):
    count = models.IntegerField()
    add_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("cook.Ingredient", on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return str(self.user) + " => " + self.ingredient.name + " : " + str(self.count) + "개"

    class Meta:
        db_table = "sumyo_refrigerator"
        verbose_name = "냉장고"
        verbose_name_plural = "냉장고"