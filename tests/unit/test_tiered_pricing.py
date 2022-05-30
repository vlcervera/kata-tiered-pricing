from app.subscriptions import IncorrectSubscriptionsAmount
from app.tier.entities import TierRange
from app.tier.exceptions import (
    MultipleTierFoundForSubscriptions,
    TierNotFoundForSubscriptions,
)
from app.tiered_pricing import TieredPricing
from tests.unit.mother import SubscriptionsMother


class TestTieredPricingShould:
    def test_calculate_price_for_subscriptions_with_price_299(self):
        pricing = TieredPricing()
        for subscriptions in range(1, 2 + 1):
            assert pricing.calculate_for(SubscriptionsMother.create(subscriptions)) == subscriptions * 299

    def test_calculate_price_for_subscriptions_with_price_239(self):
        pricing = TieredPricing()
        for subscriptions in range(3, 10 + 1):
            assert pricing.calculate_for(SubscriptionsMother.create(subscriptions)) == subscriptions * 239

    def test_calculate_price_for_subscription_with_price_219(self):
        pricing = TieredPricing()
        for subscriptions in range(11, 25 + 1):
            assert pricing.calculate_for(SubscriptionsMother.create(subscriptions)) == subscriptions * 219

    def test_calculate_price_for_subscription_with_price_199(self):
        pricing = TieredPricing()
        for subscriptions in range(26, 50 + 1):
            assert pricing.calculate_for(SubscriptionsMother.create(subscriptions)) == subscriptions * 199

    def test_calculate_price_for_subscription_with_price_149(self):
        pricing = TieredPricing()
        for subscriptions in range(51, 60 + 1):
            assert pricing.calculate_for(SubscriptionsMother.create(subscriptions)) == subscriptions * 149

    def test_error_not_found_tier_price_for_subscriptions(self):
        pricing = TieredPricing(tier_prices=(TierRange(min=1, max=2, price=299),))

        try:
            pricing.calculate_for(SubscriptionsMother.create(100))
            assert False
        except TierNotFoundForSubscriptions:
            assert True

    def test_error_for_multiple_tier_price_found_for_subscriptions(self):
        pricing = TieredPricing(
            tier_prices=(
                TierRange(min=1, max=2, price=299),
                TierRange(min=1, max=5, price=100),
            )
        )

        try:
            pricing.calculate_for(SubscriptionsMother.create(2))
            assert False
        except MultipleTierFoundForSubscriptions:
            assert True

    def test_error_for_negative_subscriptions(self):
        pricing = TieredPricing()

        try:
            pricing.calculate_for(SubscriptionsMother.create(-10))
            assert False
        except IncorrectSubscriptionsAmount:
            assert True
