# Generated by Django 3.1 on 2020-08-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submitnum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttt_ans', models.TextField()),
                ('ttt_datime', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
