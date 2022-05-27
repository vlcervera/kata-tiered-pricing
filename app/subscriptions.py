class IncorrectSubscriptionsAmount(Exception):
    def __init__(self, subscriptions: int):
        super().__init__(f"Incorrect subscriptions value ( {subscriptions} )")


class Subscriptions:
    _amount: int

    def __init__(self, amount: int):
        if amount <= 0:
            raise IncorrectSubscriptionsAmount(subscriptions=amount)
        self._amount = amount

    @property
    def amount(self):
        return self._amount
