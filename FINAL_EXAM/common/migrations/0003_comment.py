# Generated by Django 4.2.3 on 2023-08-06 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drawings', '0004_alter_drawing_kid_owner_drawing'),
        ('common', '0002_alter_like_to_drawing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('datetime_of_publication', models.DateTimeField(auto_now_add=True)),
                ('to_drawing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drawings.drawing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-datetime_of_publication'],
            },
        ),
    ]
