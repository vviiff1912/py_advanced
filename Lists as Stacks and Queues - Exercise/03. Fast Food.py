from collections import deque

food_quantity = int(input())
orders = deque([int(order) for order in input().split()])
max_order = max(orders)

while True:
    if not orders:
        break
    if orders[0] <= food_quantity:
        food_quantity -= orders.popleft()
        continue
    break

print(max_order)
if not orders:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(el) for el in orders])}")
