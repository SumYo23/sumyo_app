'''django'''
from django.db import models

'''local'''
from ai.utils import rename_imagefile_to_uuid

# Image모델
class Image(models.Model):
    image = models.ImageField(upload_to=rename_imagefile_to_uuid, max_length=255)

    def __str__(self):
        return self.image

    class Meta:
        db_table = "sumyo_image"
        verbose_name = "이미지"
        verbose_name_plural = "이미지"
