from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from datetime import datetime

from FINAL_EXAM.validators import only_letters_validator

# from FINAL_EXAM.validators import OnlyLettersValidator

UserModel = get_user_model()





class Kid(models.Model):
    MAX_NAME_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
        validators=[only_letters_validator]
    )

    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField(
        null=False,
        blank=False,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.user} {self.name}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}: {self.count_age} years old'

    @property
    def count_age(self):
        current_date = datetime.now().date()
        age = current_date.year - self.date_of_birth.year - (
                (current_date.month, current_date.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age
