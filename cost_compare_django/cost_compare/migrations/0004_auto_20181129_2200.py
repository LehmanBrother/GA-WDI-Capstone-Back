# Generated by Django 2.1.3 on 2018-11-29 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost_compare', '0003_auto_20181129_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='federal_account_raw',
            name='code',
            field=models.CharField(default=0, max_length=4),
        ),
    ]
