# Generated by Django 4.1.2 on 2022-10-20 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("categories", "0002_categorie_ingreso"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Egress",
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
                ("fecha", models.DateField(max_length=100)),
                ("descripcion", models.CharField(max_length=100)),
                ("monto", models.IntegerField()),
                (
                    "idcategoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="categories.categorie",
                    ),
                ),
                (
                    "idusuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
            ],
        ),
    ]
