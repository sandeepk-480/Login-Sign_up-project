# Generated by Django 5.0 on 2023-12-07 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_customuser_address_line_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(upload_to='profile_pic/'),
        ),
    ]
