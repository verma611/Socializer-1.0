# Generated by Django 4.1.7 on 2023-03-07 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMedia', '0003_alter_post_image_alter_post_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media/videos/'),
        ),
    ]