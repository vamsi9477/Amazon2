# Generated by Django 2.1.1 on 2018-10-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ama', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amazonwebsite',
            name='id',
        ),
        migrations.AlterField(
            model_name='amazonwebsite',
            name='cno',
            field=models.IntegerField(default=10, primary_key=True, serialize=False),
        ),
    ]
