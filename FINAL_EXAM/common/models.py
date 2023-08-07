from django.contrib.auth import get_user_model
from django.db import models

from FINAL_EXAM.drawings.models import Drawing

UserModel = get_user_model()


class Like(models.Model):
    to_drawing = models.ForeignKey(
        Drawing,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )


class Comment(models.Model):
    MAX_COMM_LEN = 300

    text = models.TextField(
        max_length=MAX_COMM_LEN,
    )

    datetime_of_publication = models.DateTimeField(
        auto_now_add=True,

    )

    to_drawing = models.ForeignKey(
        Drawing,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-datetime_of_publication']
