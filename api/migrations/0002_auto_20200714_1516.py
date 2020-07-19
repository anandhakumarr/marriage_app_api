# Generated by Django 2.2.4 on 2020-07-14 15:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('method', models.CharField(max_length=10)),
                ('request_path', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='hobbycategory',
            name='created_ts',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hobbycategory',
            name='updated_ts',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
