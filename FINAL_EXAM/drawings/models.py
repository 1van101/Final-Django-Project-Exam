from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from FINAL_EXAM.kids.models import Kid

UserModel = get_user_model()


class Drawing(models.Model):
    MAX_DESC_LEN = 300
    MIN_DESC_LEN = 10

    drawing = models.ImageField(
        upload_to='images',
    )
    description = models.TextField(
        max_length=MAX_DESC_LEN,
        null=True,
        blank=True,
        validators=(
            MinLengthValidator(MIN_DESC_LEN),
        )
    )

    kid_owner_drawing = models.ForeignKey(
        Kid,
        on_delete=models.CASCADE
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Drawing of {self.kid_owner_drawing.name}'

    class Meta:
        ordering = ['-date_of_publication']
