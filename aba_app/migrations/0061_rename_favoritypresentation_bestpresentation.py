# Generated by Django 4.1.4 on 2022-12-15 04:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aba_app', '0060_favoritypresentation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavorityPresentation',
            new_name='BestPresentation',
        ),
    ]
