# Generated by Django 5.0.3 on 2024-04-11 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]