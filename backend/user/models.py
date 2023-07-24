from django.db import models


# Create your models here.

class User(models.Model):
    user_number = models.CharField(max_length=256)
    registered_date = models.DateField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.user_number

    class Meta:
        db_table = "sumyo_user"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
