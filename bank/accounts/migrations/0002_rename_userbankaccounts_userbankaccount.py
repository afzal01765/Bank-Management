# Generated by Django 4.2.11 on 2025-05-07 08:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserBankAccounts',
            new_name='UserBankAccount',
        ),
    ]
