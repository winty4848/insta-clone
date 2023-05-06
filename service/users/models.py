from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email=self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.set_default('is_staff',True)
        extra_fields.set_default('is_superuser',True)
        extra_fields.set_default('is_active',True)
        return self.create_user(email, password, **extra_fields)

# 사용자 정보를 다루는 모델
class User(AbstractUser):
    TIMEOUT=60*5

    USERNAME_FIELD='email' #이메일이 pk
    REQUIRED_FIELDS=['username'] #가입할 때 필수
    
    email=models.EmailField(max_length=256, unique=True)
    username=models.CharField(max_length=128, unique=True)
    password=models.CharField(max_length=128, null=True, blank=True)
    profile=models.ImageField(null=False, blank=True)
    description=models.CharField(max_length=512, blank=True)
    authcode=models.CharField(max_length=17)
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    object=UserManager()
    user_manager=UserManager()