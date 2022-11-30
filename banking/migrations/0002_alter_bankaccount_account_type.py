# Generated by Django 4.0.3 on 2022-11-30 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_type',
            field=models.CharField(choices=[('savings', 'credit')], db_index=True, max_length=20),
        ),
    ]
