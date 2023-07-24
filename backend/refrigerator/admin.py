from django.contrib import admin

# Register your models here.
from user import models

admin.register(models.User)
