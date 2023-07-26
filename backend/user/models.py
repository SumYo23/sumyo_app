from django.db import models


# 사용자
class User(models.Model):
    user_number = models.TextField()
    registered_date = models.DateField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.user_number

    class Meta:
        db_table = "sumyo_user"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
