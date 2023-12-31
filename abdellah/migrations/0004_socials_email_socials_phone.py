# Generated by Django 4.2 on 2023-08-17 13:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('abdellah', '0003_socials_delete_portfolio_remove_about_career_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='socials',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='socials',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
