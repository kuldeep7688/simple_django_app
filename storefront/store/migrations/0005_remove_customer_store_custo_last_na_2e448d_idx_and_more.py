# Generated by Django 5.0.6 on 2024-07-04 05:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "store",
            "0004_rename_store_custo_last_na_e6a359_idx_store_custo_last_na_2e448d_idx_and_more",
        ),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="customer",
            name="store_custo_last_na_2e448d_idx",
        ),
        migrations.AlterModelTable(
            name="customer",
            table=None,
        ),
    ]
