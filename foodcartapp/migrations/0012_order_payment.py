# Generated by Django 3.1.4 on 2020-12-19 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0011_auto_20201219_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('CASH', 'Наличными'), ('CARD', 'Электронно')], default='CARD', max_length=125),
        ),
    ]
