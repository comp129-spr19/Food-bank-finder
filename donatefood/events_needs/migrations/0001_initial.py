# Generated by Django 2.1.7 on 2019-04-15 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodBanks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_bank_name', models.CharField(max_length=100)),
                ('food_bank_event', models.CharField(max_length=100)),
                ('food_bank_description', models.CharField(max_length=500)),
            ],
        ),
    ]
