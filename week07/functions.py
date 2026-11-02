# Q1: First bug: missing ":" on the for loop. I found it from the traceback.
#     I should read error messages more carefully.
# Q2: apply_discount takes a price and a tier and returns the price after
#     the discount (gold 15%, silver 10%, bronze 5%, else 0%).
#     Yes, a colleague could use it without reading the code.
# Q3 / AI disclosure: I used Claude to guide me through the lab and explain
#     bugs 2 and 3. It helped me understand.
# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price*rate
tax1= calculate_tax(100, 0.07)
tax2= calculate_tax(250, 0.08)
print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")

# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price*0.85
    elif tier == "silver":
        return price*0.90
    elif tier == "bronze":
        return price*0.95
    else:
        return price
print(f"gold: ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none: ${apply_discount(200, 'none'):.2f}")

# --- Exercise 3 ---
discounted = apply_discount(200, "gold")      
print(f"After gold discount: ${discounted:.2f}")
tax = calculate_tax(discounted, 0.07)         
with_tax = discounted + tax                  
print(f"After tax: ${with_tax:.2f}") 
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax
print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# --- Exercise 5 ---
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1
# Bug 1: missing ":" on the for loop -> SyntaxError
# Bug 2: <= went past the last index -> IndexError, changed to <
# Bug 3: total = sale only kept the last sale, changed to +=

# --- Exercise 6 ---
# Scope: x inside double_it() is a local variable. It only exists inside the function.
# If we change it, does not change the global x outside, so x stays 100.
x = 100

def double_it():
    x = 999
    return x * 2

print(x)            # 100
print(double_it())  # 1998
print(x)            # 100