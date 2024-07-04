# Generated by Django 5.0.6 on 2024-07-04 05:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0003_address_zip_code_and_more"),
    ]

    operations = [
        migrations.RenameIndex(
            model_name="customer",
            new_name="store_custo_last_na_2e448d_idx",
            old_name="store_custo_last_na_e6a359_idx",
        ),
        migrations.AlterModelTable(
            name="customer",
            table="store_customer",
        ),
    ]