from tabulate import tabulate
import sys

all_expenses = []
counter = 0

def main():
    print("\n\nWelcome to our Exenditure Management Program!\n\n")
    print("Follow the menu to access the app:\n")
    print(option_selection())


def display_menu():
    # The menu which will be displayed throughout the program
    menu_header = ["S.No.", "Option", "Command"]
    menu_body = [["1", "Add an Expense", "A"],
                 ["2", "Edit an Expense", "E"],
                 ["3", "Remove an Expense", "R"],
                 ["4", "View all Expenses", "V"],
                 ["5", "Exit the Program", "X"],
    ]
    return tabulate(menu_body, headers = menu_header, tablefmt = "mixed_grid", colalign=("center","left","center",))


def option_selection():
    while True:
        try:
            print(display_menu())
            choice = input("\nEnter your command: ").upper()
        except Exception:
            pass
        else:
            if choice == 'A':
                print(add_expense())
                _ = input("Enter any key to revert to the main menu: ")
            elif choice == 'E':
                print(edit_expense())
                _ = input("Enter any key to revert to the main menu: ")
                global all_expenses
            elif choice == 'R':
                print(remove_expense())
                _ = input("Enter any key to revert to the main menu: ")
            elif choice == 'V':
                print(view_expense())
                _ = input("Enter any key to revert to the main menu: ")
            elif choice == 'X':
                sys.exit("\n\nThank You for using our program!\n")
            else:
                print("\nInvalid command. \nPlease try again.")

def add_expense():
    while True:
        try:
            expense_name = input("\nExpense name: ")
            expense_amount = int(input("Expense amount: "))
            if expense_amount < 0:
                raise ValueError
        except ValueError:
            print("\nInvalid entry. Try again.")
        else:
            global counter
            counter += 1
            global all_expenses
            all_expenses.append([counter,expense_name,expense_amount])
            return "\nExpense added\n"



def edit_expense():
    global counter
    if counter == 0:
        return "\nNo entries to edit.\n"
    else:
        while True:
            try:
                edit_id = int(input("\nEnter Expense ID to be edited: "))
                if edit_id > counter or edit_id < 0:
                    raise ValueError
                elif edit_id == 0:
                    break
                edit_name = input("Expense name: ")
                edit_amount = int(input("Expense amount: "))
                if edit_amount < 0:
                    raise ValueError
            except ValueError:
                print("\nInvalid entry. Try again. \nEnter '0' to cancel.")
            else:
                global all_expenses
                for i in range(len(all_expenses)):
                    if all_expenses[i][0] == edit_id:
                        all_expenses[i][1] = edit_name
                        all_expenses[i][2] = edit_amount
                        break
                # all_expenses[edit_id - 1][1] = edit_name
                # all_expenses[edit_id - 1][2] = edit_amount
                return "\nExpense edited\n"



def remove_expense():

    global all_expenses
    global counter

    if len(all_expenses) == 0:
        return "\nNo entries to remove.\n"
    else:
        while True:
            try:
                remove_id = int(input("\nEnter Expense ID to be removed: "))
                if remove_id > counter or remove_id < 0:
                    raise ValueError
                elif remove_id == 0:
                    break
            except Exception:
                print("\nInvalid entry. Try again. \nEnter '0' to cancel.\n")
            else:
                for i in range(len(all_expenses)):
                    if all_expenses[i][0] == remove_id:
                        del all_expenses[i]
                        break
                return "\nExpense Removed\n"



def view_expense():
    global all_expenses
    global counter
    if len(all_expenses) == 0:
        return "\nNo entries to view.\n"
    view_header = ["ID", "Expense Name", "Expense Amount"]
    return tabulate(all_expenses, headers = view_header, tablefmt = "mixed_grid", colalign=("center","center","center",))

if __name__ == "__main__":
    main()