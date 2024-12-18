#Age classification
name = input("Enter your name:")
age = eval(input("Enter your age:"))

#age calssifications:

if age >=1 and age <= 8:
	print(f"Hi {name}, your age is considered Toddler.")
if age >= 9 and age <= 14:
	print(f"Hi {name}, your age is considered Preteen.")
if age >= 15 and age <= 18:
	print(f"Hi {name}, your age is considered Teenager.")
if age >= 19 and age <= 27:
	print(f"Hi {name}, your age is considered early Adulthood.")
if age >= 28 and age <= 44:
	print(f"Hi {name}, your age is considered Middle Age.")
if age >= 45 and age <=59:
	print(f"Hi {name}, your age is considered Post Adulthood.")
if age >= 60 and age <= 100:
	print(f"Hi {name}, your age is considered Senior.")

if age >=101:
	print(f"Expired ka na.")