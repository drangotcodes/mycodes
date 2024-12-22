name = input("Enter your name --->")
money = eval(input("Enter the amount that you will deposit --->"))

onekey = money // 1000
fiveh = (money - 1000) // 500
twoh = (money % 1000) % (500) // 200
oneh = (money % 1000) % (500) // (200) // 100
pipti = (money % 1000) % (500) % (200) % (100) // 50
bente = (money % 1000) % (500) % (200) % (100) % (50) // 20
sampo = (money % 1000) % (500) % (200) % (100) % (50) % (20) // 10
lima = (money % 1000) % (500) % (200) % (100) % (50) % (20) % (10) // 5
dos = (money % 1000) % (500) % (200) % (100) % (50) % (20) % (10) % (5) // 2 
piso = (money % 1000) % (500) % (200) % (100) % (50) % (20) % (10) % (5) % (2) // 1

answer = input("Would you like to see the deposited money in Ph denominations? please enter yes or no? ")
y = "yes"
n = "no"

if answer.lower() == "yes" :
	print(F"Here is your deposited money in Ph denominations:")
	print(f"{onekey} = 1000 \n{fiveh} = 500 \n{twoh} = 200 \n{oneh} = 100 \n{pipti} = 50 \n{bente} = 20 \n{sampo} = 10 \n{lima} = 5 \n{dos} = 2 \n{piso} = 1")

if answer.lower() == "no":
	print(f"Your money has been deposited!")


#draft
#print(f"{onekey} = 1000")
#print(f"{fiveh} = 500")
#print(f"{twoh} = 200")
#print(f"{oneh} = 100")
#print(f"{pipti} = 50")
#print(f"{bente} = 20")
#print(f"{sampo} = 10")
#print(f"{lima} = 5")
#print(f"{dos} = 2")
#print(f"{piso} = 1")


