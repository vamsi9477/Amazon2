# Generated by Django 2.1.1 on 2018-10-29 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ama', '0003_paymentprocesses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentprocesses',
            name='id',
        ),
        migrations.AddField(
            model_name='paymentprocesses',
            name='pcno',
            field=models.IntegerField(default=10, primary_key=True, serialize=False),
        ),
    ]
