import pytest

from app.tiered_pricing import TieredPricing
from tests.unit.mother import SubscriptionsMother


class TestTieredPricingShould:
    @pytest.mark.parametrize("subscriptions", [1, 2])
    def test_calculate_price_for_subscriptions_with_unit_price_299(self, subscriptions):
        pricing = TieredPricing()
        assert pricing.calculate_for(SubscriptionsMother.create(subscriptions)) == subscriptions * 299

    @pytest.mark.parametrize(
        "subscriptions",
        [3, 4, 5, 6, 7, 8, 9, 10],
    )
    def test_calculate_price_for_subscriptions_with_unit_price_239(self, subscriptions):
        pricing = TieredPricing()
        assert pricing.calculate_for(SubscriptionsMother.create(subscriptions)) == subscriptions * 239

    @pytest.mark.parametrize(
        "subscriptions",
        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
    )
    def test_calculate_price_for_subscriptions_with_unit_price_219(self, subscriptions):
        pricing = TieredPricing()
        assert pricing.calculate_for(SubscriptionsMother.create(subscriptions)) == subscriptions * 219

    @pytest.mark.parametrize(
        "subscriptions",
        [
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            45,
            50,
        ],
    )
    def test_calculate_price_for_subscriptions_with_unit_price_199(self, subscriptions):
        pricing = TieredPricing()
        assert pricing.calculate_for(SubscriptionsMother.create(subscriptions)) == subscriptions * 199

    @pytest.mark.parametrize(
        "subscriptions",
        [51, 55, 60, 100, 200, 600],
    )
    def test_calculate_price_for_subscriptions_with_unit_price_149(self, subscriptions):
        pricing = TieredPricing()
        assert pricing.calculate_for(SubscriptionsMother.create(subscriptions)) == subscriptions * 149
