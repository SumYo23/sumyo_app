from django.db import models


# Create your models here.

class Like(models.Model):
    cook = models.ForeignKey("Cook", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user_number + " likes " + self.cook.name

    class Meta:
        db_table = "sumyo_refrigerator"
        verbose_name = "냉장고"
        verbose_name_plural = "냉장고"