from django.contrib import admin

# Register your models here.
from cook import models

admin.register(models.Cook)
admin.register(models.Ingredient)
admin.register(models.Recipe)