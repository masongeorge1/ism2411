
def calculate_tax(price, rate):
    return price * rate

def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0

    return price * (1 - discount)

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")

total = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${total:.2f}")

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")
