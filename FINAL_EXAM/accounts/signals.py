from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

UserModel = get_user_model()


@receiver(signal=post_save, sender=UserModel)
def send_email_on_successful_register(instance, created, **kwargs):
    if not created:
        return

    email_content = render_to_string('email-greeting.html', {
        'user': instance,
    })

    send_mail(
        subject='Hello!',
        message=strip_tags(email_content),
        html_message=email_content,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(instance.email,),
    )
