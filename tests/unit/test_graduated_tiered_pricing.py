import pytest

from app.graduated_tiered_pricing import GraduatedTieredPricing
from app.subscriptions import IncorrectSubscriptionsAmount
from app.tier.entities import TierRange
from app.tier.exceptions import MultipleTierFoundForSubscriptions
from app.tiered_pricing import TieredPricing
from tests.unit.mother import SubscriptionsMother


class TestGraduatedTieredPricingShould:
    @pytest.mark.parametrize(
        "subscriptions, total_price",
        [
            (1, 299),
            (2, 598),
            (3, 837),
            (4, 1076),
            (5, 1315),
            (11, 2729),
            (12, 2948),
            (13, 3167),
            (26, 5994),
            (27, 6193),
            (28, 6392),
            (50, 10770),
            (51, 10919),
            (52, 11068),
        ],
    )
    def test_calculate_graduated_tiered_pricing_for_acceptance_criteria_requirements(self, subscriptions, total_price):
        pricing = GraduatedTieredPricing()
        assert pricing.calculate_for(SubscriptionsMother.create(subscriptions)) == total_price

    def test_error_for_negative_subscriptions(self):
        pricing = GraduatedTieredPricing()

        with pytest.raises(IncorrectSubscriptionsAmount):
            pricing.calculate_for(SubscriptionsMother.create(-10))

    def test_error_for_multiple_tier_price_found_for_subscriptions(self):
        pricing = TieredPricing(
            tier_prices=(
                TierRange(min=1, max=2, price=299),
                TierRange(min=1, max=5, price=100),
            )
        )

        with pytest.raises(MultipleTierFoundForSubscriptions):
            pricing.calculate_for(SubscriptionsMother.create(2))
