# Generated by Django 4.2.3 on 2023-08-11 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_appuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True),
        ),
    ]
