# %%

orders = [
    {
        "customer": "Ahmet",
        "items": ["Laptop", "Mouse", "Mouse"],
        "total": 18500,
        "is_paid": True
    },

    {
        "customer": "Zeynep",
        "items": ["Keyboard"],
        "total": 2500,
        "is_paid": False
    },

    {
        "customer": "Mehmet",
        "items": ["Monitor", "HDMI Cable", "Monitor"],
        "total": 7200,
        "is_paid": True
    }
]

# %%
# Cell 2 – Order Count Analysis

total_orders = len(orders)

paid_orders = 0
unpaid_orders = 0

for order in orders:
    if order["is_paid"] == True:
        paid_orders += 1
    else:
        unpaid_orders += 1

print("Total number of orders:", total_orders)
print("Paid orders:", paid_orders)
print("Unpaid orders:", unpaid_orders)

# %%
# Cell 3 - Customer List

customer_list = [ ]

for order in orders:
    customer_list.append(order["customer"])

    unique_customers = set(customer_list)

print("All customers:", customer_list)
print("Unique customers:", unique_customers)

# %%
# Cell 4 - Product Analysis

product_list = []

for order in orders :
    for item in order["items"]:
       product_list.append(item)
  

       unique_products = set(product_list)

print("All products:", product_list)
print("Pepeated products included above.,")
print("Unique products:", unique_products)


# %%
# Cell 5 – Order Status check

for order in orders:
    if order["is_paid"] == True:
        print(order["customer"], "-", "Order confirmed")
    else:
        print(order["customer"], "-", "Payment pending")

# %%
# Cell 6 - Tuple

# Tuple is immutable, which means its values cannot be changed after creation.
# This makes it safer for fixed data like customer name + total amount.

order_summary = []

for order in orders:
    summary = (order["customer"], order["total"])
    order_summary.append(summary)

print("Secure order summaries:", order_summary)

# 

# order_summary = []

# for order in orders:
#     summary = (order["customer"], order["total"])
#     order_summary.append(summary)

# %%
# Final Cell – General Outputs

print("Total orders:", total_orders)
print("Paid orders:", paid_orders)
print("Unpaid orders:", unpaid_orders)

print()

print("Unique products:", unique_products)
print("Order summaries:", order_summary)