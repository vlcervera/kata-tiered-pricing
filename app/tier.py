from abc import ABC, abstractmethod

from subscriptions import Subscriptions


class Tier(ABC):
    price: int

    @abstractmethod
    def applies_to(self, subscriptions: int) -> bool:
        pass


class TierFrom(Tier):
    min: int

    def __init__(self, min: int, price: int):
        self.min = min
        self.price = price

    def applies_to(self, subscriptions: Subscriptions) -> bool:
        return self.min <= subscriptions.amount


class TierRange(Tier):
    min: int
    max: int

    def __init__(self, min: int, max: int, price: int):
        self.min = min
        self.max = max
        self.price = price

    def applies_to(self, subscriptions: Subscriptions) -> bool:
        return self.min <= subscriptions.amount <= self.max
