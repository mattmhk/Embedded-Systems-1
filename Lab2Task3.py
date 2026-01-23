cover_price = 25.00
discount_perc = 40
fixed_delivery_cost = 5.50
unit_delivery_cost = 0.55
order_qty = 350
cost_of_books = cover_price * order_qty * (100 - discount_perc) / 100
delivery_cost = fixed_delivery_cost + unit_delivery_cost * order_qty
print("The final order price is :", cost_of_books + delivery_cost)
print("The order details are as follows:")
print("Cost of books: $", cost_of_books)
print("Delivery cost: $", delivery_cost)