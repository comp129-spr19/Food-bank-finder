# Generated by Django 2.1.7 on 2019-04-23 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_needs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodbankevents',
            name='food_bank_name',
            field=models.CharField(default='Food Bank Name', max_length=100),
        ),
    ]
