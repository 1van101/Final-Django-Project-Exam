from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models


from FINAL_EXAM.validators import only_letters_validator


class AppUser(auth_models.AbstractUser):
    MIN_USERNAME_LEN = 2
    MAX_USERNAME_LEN = 30
    MAX_FNAME_LEN = 30
    MAX_LNAME_LEN = 30
    MIN_FNAME_LEN = 2
    MIN_LNAME_LEN = 2
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        unique=True,
        validators=[MinLengthValidator(limit_value=MIN_USERNAME_LEN,
                                       message='Ensure username has at least 2 characters (it has 1).')],
    )

    first_name = models.CharField(
        max_length=MAX_FNAME_LEN,
        validators=[
            MinLengthValidator(MIN_FNAME_LEN),
            only_letters_validator
        ],
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=MAX_LNAME_LEN,
        validators=[
            MinLengthValidator(MIN_LNAME_LEN),
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

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        return self.username

