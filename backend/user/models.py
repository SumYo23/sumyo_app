# accounts/model.py

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, user_number, password="sumyo"):
        user = self.model(
            user_number=user_number,
            user_number_repeat=user_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_number, user_number_repeat, password="sumyo"):
        user = self.model(
            user_number=user_number,
            user_number_repeat=user_number,
        )
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_number = models.TextField(unique=True)
    user_number_repeat = models.TextField(unique=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_number'
    REQUIRED_FIELDS = ['user_number_repeat']

    def __str__(self):
        return self.user_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'sumyo_user'  # 테이블명을 user로 설정

