import os
tuloy = True

def greet():
    os.system('cls')
    global name
    global start
    print(f"\t\t\tHi im Codequiz!")
    print(f"\t\"I'm a program that will teach you about phyton,\n\t\t in a way that you will enjoy it\"")
    print(f"Firts thing first let us know your name!")
    name = input("Name = ")
    print(f"Hi {name}, lets get started?")
    start = input("yes/no: ")
    while tuloy == True:
        if start.lower() == "yes":
            show_menu()
        elif start.lower() == "no":
            print(f"See you when you're ready!")
            break
        else:
            print(f"Invalid input, The program will end.")
            break

def show_menu():
    os.system('cls')
    global tuloy
    print(f"\tWelcome to Codequiz!")
    print(f"\nTopics:")
    print(f"1. Print Statements.")
    print(f"2. Variables.")
    print(f"3. Conditional Statements.")
    print(f"4. Loops.")
    print(f"5. Functions.")
    print(f"6. List.")
    print(f"7. Assignment Operators.")
    print(f"8. Exit.")
    while tuloy == True:
        choice = input("Choose a topic to learn: ")
        if choice == "1":
            learn_print_statements()
        elif choice == "2":
            learn_variables()
        elif choice == "3":
            learn_conditionals()
        elif choice == "4":
            learn_loops()
        elif choice == "5":
            learn_functions()
        elif choice == "6":
            learn_lists()
        elif choice == "7":
            learn_assignment_operators()
        elif choice == "8":
            print(f"\nThank you for learning with me, Codequiz! Til we meet again Goodbye!.")
            tuloy = False
        else:
            print(f"\nInvalid choice. Please select a valid option.")



def learn_print_statements():
    os.system('cls')
    global a
    print(f"\nPrint statements are used to display output. To print something we use \"print()\" For example:")
    print(f"\nprint(\"Hello, World!\")")
    print(f"""
The output of this code would be "Hello, World!"
When using print function always remember to use string formatting to do this just remember to put an "f" before your quotation
Example:
    print(f"Hello World")

This just help you to make your printing easier""")
    a=input("Press enter or type any key to continue. ")
    print_prob()



def print_prob():   
    os.system('cls')
    global tuloy
    global tryprint
    global pili
    global b
    global cont
    print(f"""Try it yourself, try printing this:
          Good Day!""")
    tryprint = input("")
    if tryprint == "print(f\"Good Day!\")":
        print(f"Good Day!")
        print(f"""Congrats you have done it!""")
        print(f"""You have learned to Print statements!.""")
        cont=input("\nPress Enter or any key to continue.\n")
        what_to_do()
    else:
        print(f"Awww too bad there is an error in your code!\nBut its okay you're still learning!") 
        pili = input("""What do you want to do now?
1. Try Problem again.
2. Learn Variables.
3. Learn Conditional Statements.
4. Learn Loops.
5. Learn Functions.
6. Learn List.
7. Learn Assignment Operators.
8. Exit Program.
""")
        if pili == "1":
            print_prob()
        elif pili == "2":
            learn_variables()
        elif pili == "3":
            learn_conditionals()
        elif pili == "4":
            learn_loops()
        elif pili == "5":
            learn_functions()
        elif pili == "6":
            learn_lists()
        elif pili == "7":
            learn_assignment_operators()
            print(f"\nThank you for learning with me, Codequiz! Til we meet again Goodbye!.")
            tuloy = False
        else:
            print(f"""Incorrect Choice!
The program will return to Menu.""")
            b=input("\nPress enter or type any key to continue. ")
            show_menu()       



def learn_print_statements_x_variables():
    os.system('cls') 
    global cont
    print(f"\nYou can also use print statements to display variables, to do this we use \"""{""name""}""\".\tExample in this code the \"name\" already have an set input so we'll just have to print it.")
    print(f"\nname = \"Alice\"\nprint(f\"My name is ""{""name""}"".\")Then the output of this code will be:")
    print(f"\nMy name is ""{""Alice""}"".")
    cont=input(f"\nPress enter or any key to continue. ")
    var_prob()



def var_prob():
    os.system('cls')
    global c
    global vp
    global cont
    global tuloy
    print(f"Try to solve this problem:\nname = Monkey D. Luffy\ngoal = To be the pirate king\nprint(f""Hi ""{""name""}"", your goal is ""{""goal""}"",. \")\nthe correct print-> ")
    vp=input("")
    if vp == 'print(f"Hi {name} your goal is , goal ,. ")':
        print(f"""Congrats you have done it!""")
        print(f"""You have learned to Variables!.""")
        cont=input("\nPress Enter or any key to continue.")
        learn_print_statements_x_variables()
    else:
        print(f"Awww too bad there is an error in your code!\nBut its okay you're still learning!") 
        nxt = input("""What do you want to do now?
1. Try Problem again.
2. Learn Print Statements.
3. Learn Conditional Statements.
4. Learn Loops.
5. Learn Functions.
6. Learn List.
7. Learn Assignment Operators.
8 .Exit Program.
""")
        if nxt == "1":
            var_prob()
        elif nxt == "2":
            learn_print_statements()
        elif nxt == "3":
            learn_conditionals()
        elif nxt == "4":
            learn_loops()
        elif nxt == "5":
            learn_functions()
        elif nxt == "6":
            learn_lists()
        elif nxt == "7":
            learn_assignment_operators()
        elif nxt == "8":
            print(f"\nThank you for learning with me, Codequiz! Til we meet again Goodbye!.")
            tuloy = False
        else:
            print(f"""Incorrect Choice!
The program will return to Menu.""")
            c=input("\nPress enter or type any key to continue. ")
            show_menu()       



def learn_variables():
    os.system('cls')
    global c2
    print(f"Variables are used to store data. For example:")
    print(f"name = input(\"What is your name? \")")
    print(f"age = eval(input(\"How old are you? \")")
    print(f"print(f\"Hi ""{""name""}"" you are ""{""age""}"" yrs old. \")")
    print(f"If you entered in name is Luffy and in age is 19 output of this code would be\nHi Luffy you are 19 yrs old.")
    c2=input("\nPress enter or type any key to continue. ")
    learn_print_statements_x_variables()



def learn_conditionals():
    os.system('cls')
    global d
    print(f"Conditional statements allow your program to make decisions based on conditions you give. For example:")
    print(f"""If you have an code
age = eval(input("How old are you?")
if age >= 0:
    print("You're a minor.")
elif age >= 19:
    print(f"You're an adult")
elif age >= 60:
    print("You're a senior citizen.")
elif age >= 100:
    print(f"Mamamiyaaa! You're too old")          

If you've entered 25 then the output would be "You're an adult" """)
    d=input("\nPress enter or type any key to continue. ")
    cond_prob()
    


def cond_prob():
    global c
    global cont
    global tuloy
    print(f"""Now try to create your own condition about favourite colours if the user choose red it will print mad,
if it choose yellow it means happy, if it choose white print calm.
the variable should be like this-colour = input("choose a colour from red, yellow and white")""")
    condtest = input("")
    if condtest == """colour = input("choose a colour from red, yellow and white")
age = int(input("Enter your age to see an example: "))
if colour == "red":
    print("mad")
elif clour == "yellow":
    print("happy")
elif colour == "white":
    print(f"calm")""":
        print(f"""Congrats you have done it!""")
        print(f"""You have learned to Conditional statements!.""")
        cont=input("\nPress Enter or any key to continue.")
        what_to_do()
    else:
        print(f"Awww too bad there is an error in your code!\nBut its okay you're still learning!")
        cond_prob_done = input("""What do you want to do now?
1. Try Conditionals problem again.
2. Learn Print Statements.
3. Learn Variables.
4. Learn Loops.
5. Learn Functions.
6. Learn List.
7. Learn Assignment Operators.
8. Exit Program.
""")
        if cond_prob_done == "1":
            cond_prob()
        elif cond_prob_done == "2":
            learn_print_statements()
        elif cond_prob_done == "3":
            learn_variables()
        elif cond_prob_done == "4":
            learn_loops()
        elif cond_prob_done == "5":
            learn_functions()
        elif cond_prob_done == "6":
            learn_lists()
        elif cond_prob_done == "7":
            learn_assignment_operators()
        elif cond_prob_done == "8":
            print(f"\nThank you for learning with me, Codequiz! Til we meet again Goodbye!.")
            tuloy = False
        else:
            print(f"""Incorrect Choice!
The program will return to Menu.""")
            c=input("\nPress enter or type any key to continue. ")
            show_menu()



def learn_loops():
    os.system('cls')
    global f2
    print(f"\nChoose a type of loop to learn:")
    print(f"1. For Loop")
    print(f"2. While Loop")
    print(f"3. Back to Main Menu")
    choice = input("\nEnter your choice: ")

    if choice == "1":
        learn_for_loop()
    elif choice == "2":
        learn_while_loop()
    elif choice == "3":
        show_menu()
    else:
        print(f"\nInvalid choice. Please select a valid option.")
        f2=input("\nPress enter or type any key to continue. ")
        learn_loops()



def flooptopic2():
    os.system('cls')
    global cont
    print(f"""You can also count by 2
for i in range(1, 10, 2): 
    print(i)
The output would be :
1
3
5
7
9

It counted by 2 because you add to the last range
          
You can even create shape if explore it a bit more here's an example
for i in range(1, rows + 1):
    print("* " * i)
    or it can be:
for x in range(1, 5 +1):
    for y in range(1, x +1):
        print("*", end=" ")
    print()
The output of this two code would be 
*
* *
* * *
* * * *
* * * * * 
""")
    print(f"It's kinda confusing right but i'll let you explore this one out on your own, now lets try ro solve a problem")
    cont=input("\nPress Enter or any key to continue.")
    floop_prob()



def floop_prob():
    os.system('cls')
    global g2
    global tuloy
    global floopdone
    global cont
    print(f"\nProblem: Which of the following will counts from 1 to 15")
    print(f"""A. for i in range(1, 15):
    print(i)""")
    print(f"""B. for i in range(1, 17):
    print(i)""")
    print(f"""C. for i in range(1, 16): 
    print(i""")
    answer = input("Enter your choice (A, B, or C): ")
    if answer == "C":
        print(f"Correct! The range starts at 2 and increments by 2.")
        print(f"""Congrats you have done it!""")
        print(f"""You have learned to For Loop !.""")
        cont=input("\nPress Enter or any key to continue.")
        what_to_do()
    else:
        print(f"Incorrect. The correct answer is c.")
        print(f"But its okay you're still learning!")    
        floopdone = input("""What do you want to do now?
1. Try For Loop again.
2. Learn Print Statements.
3. Learn Variables.
4. Learn Conditional Statement.
5. Learn While loop.                  
6. Learn Functions.
7. Learn List.
8. Learn Assignment Operators. 
9. Exit Program.
""")
        if floopdone == "1":
            floop_prob()
        elif floopdone == "2":
            learn_print_statements()
        elif floopdone == "3":
            learn_variables()
        elif floopdone == "4":
            learn_conditionals()
        elif floopdone == "5":
            learn_while_loop
        elif floopdone == "6":
            learn_functions()
        elif floopdone == "7":
            learn_lists()
        elif floopdone == "8":
            learn_assignment_operators()
        elif floopdone == "9":
            print(f"\nThank you for learning with me, Codequiz! Til we meet again Goodbye!.")
            tuloy = False
        else:
            print(f"""Incorrect Choice!
The program will return to Menu.""")
            g2=input("\nPress enter or type any key to continue. ")
            show_menu()



def learn_for_loop():
    os.system('cls')
    global g
    print(f"\nFor loops are used to iterate over a sequence. For example:")
    print(f"for i in range(1, 6):\n\tprint(i)")
    print(f"""This loop will count from 1 to 5:
if only count 1 to 5 because in 1 it started counting from 0.
Here's the output of the code:""")
    for i in range(1, 6):
        print(i)
    g=input("\nPress enter or type any key to continue. ")
    flooptopic2()



def learn_while_loop():
    os.system('cls')
    global cont
    print(f"\nWhile loops are used to repeat a block of code as long as a condition is true. For example:")
    print(f"counter = 1\nwhile counter <= 5:\n\tprint(counter)\n\tcounter += 1")
    print(f"""This loop will count from 1 to 5:
          Heres the code output:""")
    counter = 1
    while counter <= 5:
        print(counter)
        counter += 1
    cont=input("\nPress Enter or any key to continue.")
    print(f"\nYou can stop a while loop using a break statement. For example:")
    print(f"while True:\n\tresponse = input(\"Type 'stop' to end the loop: \")\n\tif response == 'stop':\n\t\tbreak")

    print(f"Try it now:")
    while True:
        response = input("Type 'stop' to end the loop: ")
        if response.lower() == "stop":
            print(f"Loop stopped.")
            print(f"Congrats you have stop the loop.")
            cont=input("\nPress Enter or any key to continue.")
            wloop_prob()
            break



def wloop_prob():
    os.system('cls')
    global h
    global cont
    print(f"\nHere is another problem:\n What will happen when this while loop print?")
    print(f"\ncode = 5\nwhile code > 0:\n\tprint(code)\n\tcode -= 1")
    print(f"a. 1 2 3 4 5")
    print(f"b. 5 4 3 2 1")
    print(f"c. Infinite Loop")
    sagot = input("Enter your choice (a, b, or c): ")
    if sagot == "b":
        print(f"Correct! The code decrements by 1 until it reaches 0.")
        print(f"Congrats you have done it!")
        print(f"You have learned to print statements!.")
        cont=input("\nPress Enter or any key to continue.")
        what_to_do()
    else:
        print(f"Incorrect. The correct answer is B.")
        print(f"But its okay you're still learning!")
        wloopdone = input("""What do you want to do now?
1. Try While Loop again.
2. Learn Print Statements.
3. Learn Variables.
4. Learn Conditional Statement.
5. Learn For Loop.
6. Learn Functions.
7. Learn List.
8. Learn Assignment Operators.
9. Exit Program.
""")
        if wloopdone == "1":
            wloop_prob()
        elif wloopdone == "2":
            learn_print_statements()
        elif wloopdone == "3":
            learn_variables()
        elif wloopdone == "4":
            learn_conditionals()
        elif wloopdone == "5":
            learn_for_loop()
        elif wloopdone == "6":
            learn_functions()
        elif wloopdone == "7":
            learn_lists()
        elif wloopdone == "8":
            learn_assignment_operators()
        elif wloopdone == "9":
            print(f"\nThank you for learning with me, Codequiz! Til we meet again Goodbye!.")
            tuloy = False
        else:
            print(f"""Incorrect Choice!
The program will return to Menu.""")
            h=input("\nPress enter or type any key to continue. ")
            show_menu()



def learn_assignment_operators():
    os.system('cls')
    global cont
    global h
    global tuloy
    print(f"""Assignment operators are used to assign values to variables, often in combination with arithmetic or other operations.
Here are examples of the most commonly used assignment operators in Python:
x = 10  # Assigns the value 10 to the variable x
print(x)  # Output: 10
          
We can also Add and Assign (+=):
x = 10
x += 5  # Equivalent to x = x + 5
print(x)  # Output: 15

Subtract and Assign (-=): 
x = 10
x -= 3  # Equivalent to x = x - 3
print(x)  # Output: 7

Multiply and Assign (*=):
x = 4
x *= 2  # Equivalent to x = x * 2
print(x)  # Output: 8

Divide and Assign (/=):
x = 9
x /= 3  # Equivalent to x = x / 3
print(x)  # Output: 3.0

Floor Divide and Assign (//=):
x = 9
x //= 4  # Equivalent to x = x // 4
print(x)  # Output: 2

Modulus and Assign (%=):
x = 10
x %= 3  # Equivalent to x = x % 3
print(x)  # Output: 1

Exponent and Assign (**=):
x = 3
x **= 2  # Equivalent to x = x ** 2
print(x)  # Output: 9
""")
    print(f"""If a code is 
x = 1
x += 10
x += 9
x /= 2
print(x)""")
    solve= input("What would be the solution?")
    if solve == "10":
        print(f"You are right")
        print(f"""Congrats you have done it!""")
        print(f"""You have learned to Assignment Operators!.""")
        cont=input("Press Enter or any key to continue.")
        what_to_do
    else:
        print(f"Your answer is wrong.")
        print(f"But that's okay you can still to learn this repeatedly")
        ass_op = input("""What do you want to do now?
1. Try Assignment Operators again.
2. Learn Print Statements.
3. Learn Variables.
4. Learn Conditional Statement.
5. Learn Loops.
6. Learn Functions.
7. Learn List.
8. Exit Program.
""")
        if ass_op == "1":
            learn_assignment_operators()
        elif ass_op == "2":
            learn_print_statements()
        elif ass_op == "3":
            learn_variables()
        elif ass_op == "4":
            learn_conditionals()
        elif ass_op == "5":
            learn_loops()
        elif ass_op == "6":
            learn_functions()
        elif ass_op == "7":
            learn_lists()
        elif ass_op == "8":
            print(f"\nThank you for learning with me, Codequiz! Til we meet again Goodbye!.")
            tuloy = False
        else:
            print(f"""Incorrect Choice!
The program will return to Menu.""")
            h=input("\nPress enter or type any key to continue. ")
            show_menu()



def learn_functions():
    os.system('cls')
    global cont
    print(f"\nFunctions are reusable blocks of code. You can create a function by using def sample():. For example:")
    print(f"def greet_user(user_name):\n\treturn f\"Hello, ""{""user_name""}""! Nice to meet you. ")
    print(f"""You can also add every other tools in function like looping and conditionals statement. Here's an example:
def reverse_string():
    word=input("Give a word: ")
    print(f"The word you have given is """ "{""word}"" """)
    print(f"""\trvrs=input("Do you want to reverse your word? ")
    haba=len(word)
    if rvrs.lower() == "yes":
    print(word[len(word):0:-1] + word[0])
    
To call this function we simply just use it's name with a parenthesis like this:
    reverse_string()""")

    print(f"Now you have learned it you can try it on your own code.")
    cont=input("\nPress Enter or any key to continue.")
    funcdone = input("""What do you want to do now?
1. Learn Funtions again.
2. Learn Print Statements.
3. Learn Variables.
4. Learn Conditional Statement.
5. Learn For Loop.
6. Learn List.
7. Learn Assignment Operators.
8. Exit Program.
""")
    if funcdone == "1":
        learn_functions()
    elif funcdone == "2":
           learn_print_statements()
    elif funcdone == "3":
        learn_variables()
    elif funcdone == "4":
        learn_conditionals()
    elif funcdone == "5":
        learn_for_loop()
    elif funcdone == "6":
        learn_lists()
    elif funcdone == "7":
        learn_assignment_operators()
    elif funcdone == "8":
        print(f"\nThank you for learning with me, Codequiz! Til we meet again Goodbye!.")
        tuloy = False
    else:
        print(f"Incorrect Choice!\nThe program will return to Menu.")
        l=input("\nPress enter or type any key to continue. ")
        show_menu()
    


def learn_lists():
    os.system('cls')
    global cont
    global tuloy
    print(f"\nLists are used to store multiple items. For example:")
    print(f"favorite_foods = []\nfor i in range(3):\n\tfood = input(f\"Food {i + 1}: \")\n\tfavorite_foods.append(food)")
    favorite_foods = []
    print(f"Tell me three of your favorite foods.")
    for i in range(3):
        food = input("Food {i + 1}: ")
        favorite_foods.append(food)

    print(f"\nHere's the list of your favorite foods:")
    for food in favorite_foods:
        print(f"- {food}")
    print(f"Congrats on learning list!")
    cont=input("\nPress Enter or any key to continue.")
    listdone = input("""What do you want to do now?
1. Learn List again.
2. Learn Print Statements.
3. Learn Variables.
4. Learn Conditional Statement.
5. Learn For Loop.
6. Learn Functions.
7. Learn Assignment Operators.
8. Exit Program.
""")
    if listdone == "1":
        learn_lists()
    elif listdone == "2":
           learn_print_statements()
    elif listdone == "3":
        learn_variables()
    elif listdone == "4":
        learn_conditionals()
    elif listdone == "5":
        learn_for_loop()
    elif listdone == "6":
        learn_functions()
    elif listdone == "7":
        learn_assignment_operators()
    elif listdone == "8":
        print(f"\nThank you for learning with me, Codequiz! Til we meet again Goodbye!.")
        tuloy = False
    else:
        print(f"Incorrect Choice!\nThe program will return to Menu.")
        l=input("\nPress enter or type any key to continue. ")
        show_menu()



def what_to_do():
    global gagawin
    global tuloy
    gagawin=input(f""""What do want to do now?
1. Learn Print Statements.
2. Learn Variables.
3. Learn Conditional Statements.
4. Learn Loops.
5. Learn Functions.
6. Learn List.
7. Learn Assignment Operators
8. Exit The Program.

Choose What to do: """)
    while tuloy == True:
        if gagawin == "1":
            learn_print_statements()
        elif gagawin == "2":
            learn_variables()
        elif gagawin == "3":
            learn_conditionals()
        elif gagawin == "4":
            learn_loops()
        elif gagawin == "5":
            learn_functions()
        elif gagawin == "6":
            learn_lists()
        elif gagawin == "7":
            learn_assignment_operators()
        elif gagawin == "8":
            print(f"\nThank you for learning with me, Codequiz! Til we meet again Goodbye!.")
            tuloy = False
        else:
            print(f"\nInvalid choice. Please select a valid option.")



greet()