"""Migrations for database"""

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Creates models in the database"""

    initial: bool = True

    dependencies: list = []

    operations: list = [
        migrations.CreateModel(
            name="Metal",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("metal_name", models.CharField(db_index=True, max_length=10, unique=True, verbose_name="Metal name")),
                (
                    "metal_name_en",
                    models.CharField(db_index=True, max_length=10, null=True, unique=True, verbose_name="Metal name"),
                ),
                (
                    "metal_name_ru",
                    models.CharField(db_index=True, max_length=10, null=True, unique=True, verbose_name="Metal name"),
                ),
                (
                    "metal_name_uk",
                    models.CharField(db_index=True, max_length=10, null=True, unique=True, verbose_name="Metal name"),
                ),
                ("density", models.SmallIntegerField(verbose_name="Metal density, kg/m³")),
            ],
            options={
                "verbose_name": "Metal",
                "verbose_name_plural": "Metals",
                "ordering": ("metal_name",),
            },
        ),
        migrations.CreateModel(
            name="MetalShape",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "shape_name",
                    models.CharField(db_index=True, max_length=20, unique=True, verbose_name="Profile name"),
                ),
                (
                    "shape_name_en",
                    models.CharField(db_index=True, max_length=20, null=True, unique=True, verbose_name="Profile name"),
                ),
                (
                    "shape_name_ru",
                    models.CharField(db_index=True, max_length=20, null=True, unique=True, verbose_name="Profile name"),
                ),
                (
                    "shape_name_uk",
                    models.CharField(db_index=True, max_length=20, null=True, unique=True, verbose_name="Profile name"),
                ),
            ],
            options={
                "verbose_name": "Rolled metal profile",
                "verbose_name_plural": "Rolled metal profiles",
                "ordering": ("shape_name",),
            },
        ),
        migrations.CreateModel(
            name="PageInfo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=60, unique=True, verbose_name="Page title")),
                ("title_en", models.CharField(max_length=60, null=True, unique=True, verbose_name="Page title")),
                ("title_ru", models.CharField(max_length=60, null=True, unique=True, verbose_name="Page title")),
                ("title_uk", models.CharField(max_length=60, null=True, unique=True, verbose_name="Page title")),
                ("description", models.CharField(max_length=150, verbose_name="Page description")),
                ("description_en", models.CharField(max_length=150, null=True, verbose_name="Page description")),
                ("description_ru", models.CharField(max_length=150, null=True, verbose_name="Page description")),
                ("description_uk", models.CharField(max_length=150, null=True, verbose_name="Page description")),
                ("keywords", models.CharField(max_length=250, verbose_name="Keywords")),
                ("keywords_en", models.CharField(max_length=250, null=True, verbose_name="Keywords")),
                ("keywords_ru", models.CharField(max_length=250, null=True, verbose_name="Keywords")),
                ("keywords_uk", models.CharField(max_length=250, null=True, verbose_name="Keywords")),
            ],
            options={
                "verbose_name": "Site page",
                "verbose_name_plural": "Site pages",
                "ordering": ("title",),
            },
        ),
        migrations.CreateModel(
            name="MetalAlloy",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "metal_alloy",
                    models.CharField(db_index=True, max_length=20, unique=True, verbose_name="Name of alloy"),
                ),
                (
                    "metal_alloy_en",
                    models.CharField(
                        db_index=True, max_length=20, null=True, unique=True, verbose_name="Name of alloy"
                    ),
                ),
                (
                    "metal_alloy_ru",
                    models.CharField(
                        db_index=True, max_length=20, null=True, unique=True, verbose_name="Name of alloy"
                    ),
                ),
                (
                    "metal_alloy_uk",
                    models.CharField(
                        db_index=True, max_length=20, null=True, unique=True, verbose_name="Name of alloy"
                    ),
                ),
                ("density", models.SmallIntegerField(verbose_name="Alloy density, kg/m³")),
                (
                    "metal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="metal_calc.metal", verbose_name="Metal"
                    ),
                ),
            ],
            options={
                "verbose_name": "Alloy",
                "verbose_name_plural": "Alloys",
                "ordering": ("metal", "metal_alloy"),
            },
        ),
    ]
