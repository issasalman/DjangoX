# Generated by Django 4.0 on 2021-12-08 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='_3bse',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
