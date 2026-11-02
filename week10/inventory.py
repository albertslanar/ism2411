# Reflection
# 1. What surprised me most is how simple lists are. Adding, removing, and sorting
#    items takes one short command, like .append() or .sort(), which was much easier
#    than I expected.
#
# 2. When I worked as an assistant at an accounting firm in Prague, I kept lists of
#    client documents and meetings in Excel and filtered them by hand or using excel commands. A Python list with
#    a loop and an if statement could filter or update those lists instantly.

# --- Exercise 1 ---
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# --- Exercise 2 ---
print(inventory[0])
print(inventory[-1])
middle_item=len(inventory)//2
print(inventory[middle_item])

# --- Exercise 3 ---
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# --- Exercise 4 ---
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# --- Exercise 5 ---
coords = (40.7128, -74.0060)
try:
    coords[0]=99
except TypeError as e:
    print("TypeError caught:", e)
    print("Tuples can't be changed, so coordinates stay safe from accidental edits.")
print(coords)

# --- Exercise 6 ---
sales = [100, 250, 75, 480, 200]
total=sum(sales)
count=len(sales)
average=total/count
print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

# --- Exercise 7 ---
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted=[]
for p in prices:
    discounted.append(round(p * 0.9, 2))
print("Original:", prices)
print("Discounted:", discounted)

# --- Exercise 8 ---
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales=[]
for s in sales:
    if s > 300:
        high_sales.append(s)
print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))
