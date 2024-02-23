# Generated by Django 5.0.2 on 2024-02-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(upload_to='', verbose_name='profile picture'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CREATOR', 'Creator'), ('SUBSCRIBER', 'SUBSCRIBER')], max_length=30, verbose_name='Role'),
        ),
    ]
