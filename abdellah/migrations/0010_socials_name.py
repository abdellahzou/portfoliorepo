# Generated by Django 4.2 on 2023-08-18 15:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('abdellah', '0009_rename_heading_about_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='socials',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
