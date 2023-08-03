from django.contrib.auth import get_user_model
from django.db import models

from FINAL_EXAM.drawings.models import Drawing

UserModel = get_user_model()


class Like(models.Model):
    to_drawing = models.ForeignKey(
        Drawing,
        on_delete=models.RESTRICT,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
