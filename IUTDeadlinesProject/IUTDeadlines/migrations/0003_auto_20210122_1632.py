# Generated by Django 3.1.5 on 2021-01-22 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IUTDeadlines', '0002_auto_20210121_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sophomoresubjects',
            name='day',
            field=models.ManyToManyField(to='IUTDeadlines.SophomoreDeadlines', verbose_name='list of date'),
        ),
    ]