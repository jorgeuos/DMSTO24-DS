

def calculate_discounted_total(price, quantity, discount, tax_rate):
    total = price * quantity
    discount = total * discount
    total = total - discount
    inc_vat = total * (1 + tax_rate)
    return inc_vat
   

result = calculate_discounted_total(10, 2, 0.05, 0.25)
print(result)
