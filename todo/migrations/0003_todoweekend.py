# Generated by Django 3.0.5 on 2020-05-01 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200430_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todoweekend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekendtask', models.CharField(max_length=200)),
                ('weekendis_done', models.BooleanField(default=False)),
            ],
        ),
    ]
