# Generated by Django 2.2.10 on 2021-01-11 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_poll_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='poll_id',
            new_name='poll',
        ),
    ]