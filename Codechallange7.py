#buying groceries

name = input("Enter your name: ")
groceries = input("Did you purchase groceries today? (yes / no): ")
#Conditions
if groceries.lower() == "yes" :
	item = input("What did you purchase? ")
	price = eval(input("How much is it? "))
	#All products are taxed by 12.3%
	tax = round(price * 0.123, 2)
	age = eval(input("How old are you? "))
	payment = eval(input("How much is your payment? "))
	#If the customer's payment was not enough
	if payment >= price :
	#If the purchase was over 4000 apply a 3.8% purchase discount to the untaxed price
		if price >= 4000:
			purchasediscount = round(price * 0.038, 2)
			bill = round(price - purchasediscount, 2)
			print(f"Since your purchase was over 4,000 a discount of 3.8%({purchasediscount}), is applied to your bill of {price}.")
			#If the customer is senior apply a discount of 12.3%
			if age >= 60 and age <= 100 :
				sdiscount = round(price * 0.123, 2)
				totalbill = round(bill - sdiscount, 2)
				print(f"A 12.3%({sdiscount}) senior discount is also applied to your purchase now your bill is ({totalbill}).")
				taxedbill = round(totalbill + tax, 2)
				print(f"So your bill is {totalbill}, plus a tax of 12.3%({tax}) that would be {taxedbill}")
				change = round(payment - totalbill, 2)
				print(f"You paid {payment} and your change is: {change}")
				print(f"Thank you for your purchase.")
				print(f"Please come again.")
			else :
				taxedbill = round(bill + tax, 2)
				change = round(payment - taxedbill, 2)
				print(f"So your bill now would be {bill}, plus a tax of 12.3% a toal of {taxedbill}")
				print(f"You paid {payment} and your change is: {change}")
				print(f"Thank you for your purchase.")
				print(f"Please come again.")
		else :
			#If the bill is not over 4000 but the customer is senior apply a discount
			if age >= 60 and age <= 100 :
				sdiscount = round(price * 0.123, 2)
				bill = round(price - sdiscount, 2)
				print(f"A 12.3%({sdiscount}) senior discount is also applied to your purchase now your bill is ({bill}).")
				taxedbill = round(bill + tax, 2)
				print(f"So your bill is {bill}, plus a tax of 12.3%({tax}) that would be {taxedbill}")
				change = round(payment - taxedbill, 2)
				print(f"You paid {payment} and your change is: {change}")
				print(f"Thank you for your purchase.")
				print(f"Please come again.")
			else : 
				taxedbill = round(price + tax, 2)
				print(f"Your total bill is {price} plus a tax of 12.3% a total of: {taxedbill}")
				change = round(payment - taxedbill, 2)
				print(f"You paid {payment} and your change is: {change}")		
				print(f"Thank you for your purchase.")
				print(f"Please come again.")
	else:
		print(f"Sorry your payment is not enough.")
else :
	print(f"THANK YOU!!")
	print(f"Please buy something first.")