# Generated by Django 2.1.1 on 2018-10-30 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ama', '0013_auto_20181030_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentprocesses',
            name='watchestypes',
            field=models.CharField(max_length=10),
        ),
    ]