# Generated by Django 4.2.3 on 2023-07-31 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0002_alter_kid_date_of_birth'),
        ('drawings', '0003_alter_drawing_kid_owner_drawing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawing',
            name='kid_owner_drawing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kids.kid'),
        ),
    ]
