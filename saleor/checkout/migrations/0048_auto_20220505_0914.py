# Generated by Django 3.2.12 on 2022-05-05 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0047_auto_20220505_0807"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="checkoutline",
            name="total_price_with_discounts_gross_amount",
        ),
        migrations.RemoveField(
            model_name="checkoutline",
            name="total_price_with_discounts_net_amount",
        ),
        migrations.RemoveField(
            model_name="checkoutline",
            name="undiscounted_total_price_gross_amount",
        ),
        migrations.RemoveField(
            model_name="checkoutline",
            name="undiscounted_total_price_net_amount",
        ),
        migrations.RemoveField(
            model_name="checkoutline",
            name="undiscounted_unit_price_gross_amount",
        ),
        migrations.RemoveField(
            model_name="checkoutline",
            name="undiscounted_unit_price_net_amount",
        ),
        migrations.RemoveField(
            model_name="checkoutline",
            name="unit_price_gross_amount",
        ),
        migrations.RemoveField(
            model_name="checkoutline",
            name="unit_price_net_amount",
        ),
        migrations.RemoveField(
            model_name="checkoutline",
            name="unit_price_with_discounts_gross_amount",
        ),
        migrations.RemoveField(
            model_name="checkoutline",
            name="unit_price_with_discounts_net_amount",
        ),
    ]