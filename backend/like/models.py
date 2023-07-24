from django.db import models


# Create your models here.

class Like(models.Model):
    cook = models.ForeignKey("cook.Cook", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return "likes " + self.cook.name

    class Meta:
        db_table = "sumyo_like"
        verbose_name = "좋아요"
        verbose_name_plural = "좋아요"
