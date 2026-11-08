# ISM2411 - Week 10
# Mason George
#
# Reflection 1:
# I was surprised that Python lists can hold different types of
# information and that you can change them after creating them.
# I also didn't realize how easy it was to add and remove items.
#
# Reflection 2:
# At my coffee shop job, we could use a Python list to keep track
# of daily sales. It would make it easier to calculate totals
# and averages instead of doing everything manually in Excel.


# Exercise 1 - Build the list

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))

#exercise 2 - Index Practice

print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

#Exercise 3 - slicing 

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4 - modify

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# Exercise 5 - Tuple Comparison

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed, which makes them useful for coordinates.")

print(coords)


# Exercise 6 - Average of Sales

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))


# Exercise 7 - Accumulator Pattern

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print("Original prices:", prices)
print("Discounted prices:", discounted)


# Exercise 8 - Filter Above Threshold

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales) / len(high_sales), 2))


