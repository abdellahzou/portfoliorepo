# Generated by Django 4.2 on 2023-08-18 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abdellah', '0008_rename_social_link_socials_facebook_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='heading',
            new_name='name',
        ),
    ]
