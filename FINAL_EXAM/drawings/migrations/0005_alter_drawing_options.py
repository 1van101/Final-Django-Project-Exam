# Generated by Django 4.2.3 on 2023-08-11 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drawings', '0004_alter_drawing_kid_owner_drawing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drawing',
            options={'ordering': ['-date_of_publication']},
        ),
    ]
