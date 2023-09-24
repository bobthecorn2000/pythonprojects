#!/usr/bin/env python3
import locale 
from decimal import Decimal
from decimal import ROUND_HALF_UP
locale.setlocale(locale.LC_ALL, 'en_US')
# display a title
print("The Invoice program")
print()

choice = "y"
while choice == "y":
    
    # get the user entry
    order_total = Decimal(input("Enter order total: "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()               

    # determine the discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate the results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)                                
    subtotal = order_total - discount
    tax_percent = Decimal(".05")
    shipcost = Decimal(".085")
    shipping = (subtotal * shipcost)
    shipping = shipping.quantize(Decimal("1.00"),ROUND_HALF_UP)
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)                                 
    invoice_total = subtotal + sales_tax + shipping
    order_total = locale.currency(order_total, grouping=True)
    invoice_total = locale.currency(invoice_total, grouping=True)

    spec = "10,"
    specurren = ">10"
    speclit = 20
    # display the results
    print(f"{'Order total:':{speclit}}{order_total:{specurren}}")
    print(f"{'Discount amount:':{speclit}}{discount:{spec}}")
    print(f"{'Subtotal:':{speclit}}{subtotal:{spec}}")
    print(f"{'Shipping:':{speclit}}{shipping:{spec}}")
    print(f"{'Sales tax:':{speclit}} {sales_tax:10,}")
    print(f"{'Invoice total:':{speclit}}{invoice_total:{specurren}}")
    print()

    choice = input("Continue? (y/n): ")    
    print()
    
print("Bye!")
