# Generated by Django 3.1.2 on 2021-03-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210327_0727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_membership',
            new_name='membership',
        ),
        migrations.AddField(
            model_name='userphoto',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_verified',
            field=models.BooleanField(default=False),
        ),
    ]