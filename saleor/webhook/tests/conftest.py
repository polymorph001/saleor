from decimal import Decimal
from unittest.mock import Mock, patch

import pytest


@pytest.fixture
def checkout_with_prices(
    checkout_with_items,
    address,
    address_other_country,
    warehouse,
    customer_user,
    shipping_method,
    voucher,
):
    lines = checkout_with_items.lines.all()
    for i, line in enumerate(lines, start=1):

        unit_price_net_amount = Decimal("10.000") + Decimal(i)
        unit_price_gross_amount = Decimal("10.000") + Decimal(i) * Decimal("1.100")
        line.total_price_gross_amount = unit_price_gross_amount * line.quantity
        line.total_price_net_amount = unit_price_net_amount * line.quantity

    checkout_with_items.discount_amount = Decimal("5.000")
    checkout_with_items.discount_name = "Voucher 5 USD"
    checkout_with_items.user = customer_user
    checkout_with_items.billing_address = address
    checkout_with_items.shipping_address = address_other_country
    checkout_with_items.shipping_method = shipping_method
    checkout_with_items.collection_point = warehouse
    checkout_with_items.subtotal_net_amount = Decimal("100.000")
    checkout_with_items.subtotal_gross_amount = Decimal("123.000")
    checkout_with_items.total_net_amount = Decimal("150.000")
    checkout_with_items.total_gross_amount = Decimal("178.000")
    checkout_with_items.shipping_price_net_amount = Decimal("10.000")
    checkout_with_items.shipping_price_gross_amount = Decimal("11.000")
    checkout_with_items.metadata = {"meta_key": "meta_value"}
    checkout_with_items.private_metadata = {"priv_meta_key": "priv_meta_value"}

    checkout_with_items.lines.bulk_update(
        lines,
        [
            "total_price_net_amount",
            "total_price_gross_amount",
        ],
    )

    checkout_with_items.save(
        update_fields=[
            "discount_amount",
            "discount_name",
            "user",
            "billing_address",
            "shipping_address",
            "shipping_method",
            "collection_point",
            "subtotal_net_amount",
            "subtotal_gross_amount",
            "total_net_amount",
            "total_gross_amount",
            "shipping_price_net_amount",
            "shipping_price_gross_amount",
            "metadata",
            "private_metadata",
        ]
    )

    user = checkout_with_items.user
    user.metadata = {"user_public_meta_key": "user_public_meta_value"}
    user.save(update_fields=["metadata"])

    return checkout_with_items


@pytest.fixture
def mocked_fetch_checkout():
    def mocked_fetch_side_effect(
        checkout_info, manager, lines, address, discounts, force_update=False
    ):
        return checkout_info, lines

    with patch(
        "saleor.checkout.calculations.fetch_checkout_prices_if_expired",
        new=Mock(side_effect=mocked_fetch_side_effect),
    ) as mocked_fetch:
        yield mocked_fetch


@pytest.fixture
def mocked_fetch_order():
    def mocked_fetch_side_effect(order, manager, lines, force_update=False):
        return order, lines

    with patch(
        "saleor.order.calculations.fetch_order_prices_if_expired",
        new=Mock(side_effect=mocked_fetch_side_effect),
    ) as mocked_fetch:
        yield mocked_fetch