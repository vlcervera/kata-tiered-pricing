from app.pricing.graduated_tiered_pricing import GraduatedTieredPricing
from app.vo.subscriptions import Subscriptions

print("=======================================")
print("GRADUATED TIERED PRICING APPLICATION")
print("=======================================")

pricing = GraduatedTieredPricing()
while True:

    amount_of_subscriptions = int(input("Enter the number of subscriptions that you want to buy (enter 0 to exit): "))

    if amount_of_subscriptions == 0:
        break
    subscriptions = Subscriptions(amount=amount_of_subscriptions)
    price = pricing.calculate_for(subscriptions)
    print(f"""Price={price}, for {subscriptions.amount} subscriptions""")
