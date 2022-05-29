from subscriptions import Subscriptions
from tiered_pricing import TieredPricing

pricing = TieredPricing()

while True:

    amount_of_subscriptions = int(input("Enter the number of subscriptions that you want to buy (enter 0 to exit): "))

    if amount_of_subscriptions == 0:
        break
    subscriptions = Subscriptions(amount=amount_of_subscriptions)
    price = pricing.calculate_for(subscriptions)
    print(
        f"""Price={price}, subscription/price = {price / subscriptions.amount} for {subscriptions.amount} subscriptions"""
    )
