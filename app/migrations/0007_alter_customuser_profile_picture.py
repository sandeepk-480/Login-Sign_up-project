# Generated by Django 5.0 on 2023-12-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='media/profile_pic/login_img.jpg', upload_to='profile_pic/'),
        ),
    ]
