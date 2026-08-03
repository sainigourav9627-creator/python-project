print("============== Billing System ===========")
customer_name=input("\nEnter Customer Name        : ")
product_name=input("Enter Product Name         : ")
price=int(input("Enter Price                : "))
quantity=int(input("Enter Quantity             : "))
total=price * quantity

if total>=5000:
 discount=total*(20/100)

elif total>=3000:
 discount=total*(10/100)

elif total>=1000:
 discount=total*(5/100)

else:
 discount = 0

final_amount = total - discount

print("\n================== Bill  ========================")
print(" Customer Name       : ",     customer_name)
print(" Product Name        : ",     product_name)
print(" Price               : ",     price)
print(" Quantity            : ",     quantity)
print(" Total               : ",     total)
print(" Discount            : ",     discount)
print(" Final Amount        : ",     final_amount)
