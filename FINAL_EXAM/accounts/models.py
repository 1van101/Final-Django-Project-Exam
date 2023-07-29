from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models

from FINAL_EXAM.accounts.validators import only_letters_validator

# UserModel = get_user_model()


class AppUser(auth_models.AbstractUser):
    MAX_USER_NAME_LEN = 30
    MIN_USER_NAME_LEN = 2
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    first_name = models.CharField(
        max_length=MAX_USER_NAME_LEN,
        validators=[
            MinLengthValidator(MIN_USER_NAME_LEN),
            only_letters_validator
        ],
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=MAX_USER_NAME_LEN,
        validators=[
            MinLengthValidator(MIN_USER_NAME_LEN),
            only_letters_validator
        ],
        null=True,
        blank=True
    )

    email = models.EmailField(
        unique=True
    )

    gender = models.CharField(
        choices=CHOICES,
        null=True,
        blank=True
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )

    is_visitor = models.BooleanField(default=False)


