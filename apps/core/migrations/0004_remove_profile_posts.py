# Generated by Django 5.0.4 on 2024-04-16 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_adress_profile_address_posts_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='posts',
        ),
    ]