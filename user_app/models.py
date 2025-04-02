from django.contrib.admin.models import CHANGE
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number=None, email=None, password=None, **key_value):
        if not phone_number:
            raise ValueError('Telefon raqam bo\'lishi shart.')
        if not email:
            raise ValueError('Email maydoni bo\'lishi shart.')

        key_value.setdefault("is_active", True)

        user = self.model(phone_number=phone_number, email=email, **key_value)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number=None, email=None, password=None, **key_value):
        key_value.setdefault('is_admin', True)
        key_value.setdefault('is_staff', True)
        key_value.setdefault('is_superuser', True)

        key_value.setdefault('is_active', True)

        return self.create_user(phone_number, email, password, **key_value)


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)



    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_client = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.phone_number


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=128)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.subject}"
