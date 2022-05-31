from app.vo.subscriptions import Subscriptions


class SubscriptionsMother:
    @staticmethod
    def create(subscriptions: int):
        return Subscriptions(amount=subscriptions)
