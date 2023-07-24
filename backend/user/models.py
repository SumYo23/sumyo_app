from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.

# 헬퍼 클래스
class UserManager(BaseUserManager):
    def create_user(self, user_number, **kwargs):
        """
        주어진 user_number로 User 인스턴스 생성
        """
        if not user_number:
            raise ValueError('유저 넘버를 입력해주세요')
        user = self.model(
            user_number=user_number,
        )
        user.save(using=None)
        return user

    def create_superuser(self, user_number=None, **extra_fields):
        """
        주어진 user_number로 User 인스턴스 생성 & 단, 최상위 사용자이므로 권한을 부여
        """
        superuser = self.create_user(
            user_number=user_number
        )

        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True

        superuser.save(using=None)
        return superuser


# AbstractBaseUser를 상속해서 유저 커스텀
class SumyoUser(AbstractBaseUser, PermissionsMixin):
    user_number = models.TextField(max_length=30, unique=True, null=False, blank=False)
    registered_date = models.DateField(auto_now_add=True)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 user_number으로 설정 (유저 번호로 로그인)
    USERNAME_FIELD = 'user_number'

    def __str__(self):
        return self.user_number

    class Meta:
        db_table = "sumyo_user"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"