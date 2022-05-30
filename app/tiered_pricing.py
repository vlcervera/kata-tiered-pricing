from app.subscriptions import Subscriptions
from app.tier.entities import TierFrom, TierRange
from app.tier.exceptions import (
    MultipleTierFoundForSubscriptions,
    TierNotFoundForSubscriptions,
)

TIER_PRICES = (
    TierRange(min=1, max=2, price=299),
    TierRange(min=3, max=10, price=239),
    TierRange(min=11, max=25, price=219),
    TierRange(min=26, max=50, price=199),
    TierFrom(min=51, price=149),
)


class TieredPricing:
    def __init__(self, tier_prices=TIER_PRICES):
        self.tier_prices = tier_prices

    def calculate_for(self, subscriptions: Subscriptions) -> int:
        tiers_for_subscriptions = [tier for tier in self.tier_prices if tier.applies_to(subscriptions)]
        if not tiers_for_subscriptions:
            raise TierNotFoundForSubscriptions(subscriptions)

        if len(tiers_for_subscriptions) > 1:
            raise MultipleTierFoundForSubscriptions(subscriptions)

        return subscriptions.amount * tiers_for_subscriptions[0].price
