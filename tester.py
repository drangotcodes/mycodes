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
            wloop_prob()
        elif ass_op == "2":
            learn_print()
        elif ass_op == "3":
            learn_variables()
        elif ass_op == "4":
            learn_conditionals()
        elif ass_op == "5":
            learn_loops()
        elif ass_op == "6":
            learn_functions()
        elif ass_op == "7":
            lear_list()
        elif ass_op == "8":
            print(f"\nThank you for learning with me, Codequiz! Til we meet again Goodbye!.")
            tuloy = False
        else:
            print(f"""Incorrect Choice!
The program will return to Menu.""")
            h=input("Press enter or type any key to continue. ")
            show_menu()