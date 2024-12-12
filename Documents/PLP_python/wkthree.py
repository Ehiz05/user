def calc_rebate(price, rebate_percentage):
    
    if rebate_percentage >= 20:
        discount_amount = price * (rebate_percentage / 100)
        final_price = price - discount_amount
        return final_price
    return price


original_price = 100  
discount_percentage = 25  

final_price = calc_rebate(original_price, discount_percentage)


if final_price < original_price:
    print(f"Item(s) Discounted! The final price is: ${final_price:.2f}")
else:
    print(f"Discount Unavailable. The original price is: ${original_price:.2f}")
