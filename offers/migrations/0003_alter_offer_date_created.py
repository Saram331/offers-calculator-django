# Generated by Django 5.1.5 on 2025-02-10 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0002_offer_offeritem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
