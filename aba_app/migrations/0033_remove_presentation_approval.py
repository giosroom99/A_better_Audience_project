# Generated by Django 4.1.3 on 2022-11-22 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aba_app', '0032_alter_presentation_approval'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentation',
            name='approval',
        ),
    ]
