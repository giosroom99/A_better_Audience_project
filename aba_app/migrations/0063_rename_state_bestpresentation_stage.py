# Generated by Django 4.1.4 on 2022-12-15 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0062_bestpresentation_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bestpresentation',
            old_name='state',
            new_name='stage',
        ),
    ]
