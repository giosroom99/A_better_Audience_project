# Generated by Django 4.1.3 on 2022-11-21 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0023_alter_evaluation_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluation',
            old_name='user',
            new_name='evalution_owner',
        ),
    ]
