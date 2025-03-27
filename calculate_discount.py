
def calculate_discount(price, discount_percent):
  """
  Calculates the final price after applying a discount.

  """
  if discount_percent >= 20:
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount
    return final_price
  else:
    return price

# Get user input
try:
    price = float(input("Enter price of the item: "))
    discount_percent = float(input("Enter discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Final price after discount: {final_price:.2f}")
    else:
        print(f"Original price (no discount applied): {final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")



