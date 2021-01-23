# Generated by Django 3.1.5 on 2021-01-22 12:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('IUTDeadlines', '0003_auto_20210122_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sophomoresubjects',
            name='day',
        ),
        migrations.AddField(
            model_name='sophomoresubjects',
            name='day',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='IUTDeadlines.sophomoredeadlines'),
            preserve_default=False,
        ),
    ]