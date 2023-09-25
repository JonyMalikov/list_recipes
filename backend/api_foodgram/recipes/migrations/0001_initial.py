# Generated by Django 4.2.5 on 2023-09-07 09:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Favorite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "Избранный",
                "verbose_name_plural": "Избранные",
            },
        ),
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Название")),
                (
                    "measurement_unit",
                    models.CharField(max_length=200, verbose_name="Единицы измерения"),
                ),
            ],
            options={
                "verbose_name": "Ингредиент",
                "verbose_name_plural": "Ингредиенты",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=200, verbose_name="Название"
                    ),
                ),
                ("text", models.TextField(verbose_name="Описание")),
                (
                    "cooking_time",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="Время приготовления",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="recipe_images/%Y/%m/%d/", verbose_name="Картинка"
                    ),
                ),
                (
                    "time_create",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Время создания"
                    ),
                ),
            ],
            options={
                "verbose_name": "Рецепт",
                "verbose_name_plural": "Рецепты",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="RecipeIngredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="Количество ингредиента",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ингредиент",
                "verbose_name_plural": "Ингредиенты",
                "ordering": ["recipe"],
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=200, unique=True, verbose_name="Название"
                    ),
                ),
                (
                    "color",
                    models.CharField(max_length=7, unique=True, verbose_name="Цвет"),
                ),
                (
                    "slug",
                    models.SlugField(max_length=200, unique=True, verbose_name="URL"),
                ),
            ],
            options={
                "verbose_name": "Ярлык",
                "verbose_name_plural": "Ярлыки",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="ShoppingList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipes_shopping_list",
                        to="recipes.recipe",
                        verbose_name="Список покупок",
                    ),
                ),
            ],
            options={
                "verbose_name": "Список покупок",
                "verbose_name_plural": "Списки покупок",
            },
        ),
    ]
