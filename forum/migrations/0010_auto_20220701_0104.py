# Generated by Django 3.2 on 2022-07-01 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_forumpostcomment_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forumpost',
            old_name='excerpt',
            new_name='summary',
        ),
        migrations.RenameField(
            model_name='forumtopics',
            old_name='excerpt',
            new_name='summary',
        ),
    ]