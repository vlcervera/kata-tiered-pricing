from subscriptions import Subscriptions
from tiered_pricing import TieredPricing

pricing = TieredPricing()
for amount in range(1, 55):
    subscriptions = Subscriptions(amount=amount)
    price = pricing.calculate_for(subscriptions)
    print(
        f"""Price={price}, subscription/price = {price / subscriptions.amount} for {subscriptions} subscriptions"""
    )
