# Generated by Django 2.2.10 on 2021-01-11 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210111_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='poll',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.Poll'),
        ),
    ]
