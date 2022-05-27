from subscriptions import Subscriptions


class TierNotFoundForSubscriptions(Exception):
    def __init__(self, subscriptions: Subscriptions):
        super().__init__(
            f" Tier price not found for {subscriptions.amount} subscriptions"
        )


class MultipleTierFoundForSubscriptions(Exception):
    def __init__(self, subscriptions: Subscriptions):
        super().__init__(
            f" Multiple Tier prices found for {subscriptions.amount} subscriptions"
        )
