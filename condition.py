# Question 1
def calculate_final_price(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        print(f"Original Price: {price}")
        print(f"Discount Applied: {discount_percent}%")
        print(f"Discount Amount: {discount_amount}")
        print(f"Final Price: {final_price}")
        return final_price
    else:
        print(f"No discount applied (Discount was only {discount_percent}%).")
        print(f"Final Price: {price}")
        return price
    
# Question 2
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price