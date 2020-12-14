# Generated by Django 3.1.4 on 2020-12-13 21:15

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(max_length=100)),
                ("lastname", models.CharField(max_length=100)),
                (
                    "phonenumber",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region="RU"
                    ),
                ),
                ("address", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=50, verbose_name="название"),
                ),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.CreateModel(
            name="Restaurant",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=50, verbose_name="название"),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="адрес"
                    ),
                ),
                (
                    "contact_phone",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        verbose_name="контактный телефон",
                    ),
                ),
            ],
            options={
                "verbose_name": "ресторан",
                "verbose_name_plural": "рестораны",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=50, verbose_name="название"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=8, verbose_name="цена"
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to="", verbose_name="картинка"),
                ),
                (
                    "special_status",
                    models.BooleanField(
                        db_index=True,
                        default=False,
                        verbose_name="спец.предложение",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=200, verbose_name="описание"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="foodcartapp.productcategory",
                        verbose_name="категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "товар",
                "verbose_name_plural": "товары",
            },
        ),
        migrations.CreateModel(
            name="OrderProduct",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="foodcartapp.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="foodcartapp.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="ordered_products",
            field=models.ManyToManyField(
                related_name="source", to="foodcartapp.OrderProduct"
            ),
        ),
        migrations.CreateModel(
            name="RestaurantMenuItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "availability",
                    models.BooleanField(
                        db_index=True, default=True, verbose_name="в продаже"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="menu_items",
                        to="foodcartapp.product",
                    ),
                ),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="menu_items",
                        to="foodcartapp.restaurant",
                    ),
                ),
            ],
            options={
                "verbose_name": "пункт меню ресторана",
                "verbose_name_plural": "пункты меню ресторана",
                "unique_together": {("restaurant", "product")},
            },
        ),
    ]
