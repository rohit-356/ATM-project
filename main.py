"""
ATM System — Main Entry Point
No business logic here; everything is delegated to the atm package.
"""

from atm import Account, show_menu, get_choice
from atm import display_balance, deposit, withdraw, print_statement


def main():
    print("\n  Welcome to the ATM System!")
    name = input("  Enter account holder name: ").strip()

    # Create an account with an optional opening balance
    try:
        balance = float(input("  Enter opening balance: Rs."))
    except ValueError:
        balance = 0

    account = Account(holder_name=name, initial_balance=balance)
    print(f"\n  [SUCCESS] Account created for {name} with balance Rs.{balance:,.2f}")

    # ---- Infinite loop menu system ----
    while True:
        show_menu()
        choice = get_choice()

        if choice == "1":
            display_balance(account)
        elif choice == "2":
            deposit(account)
        elif choice == "3":
            withdraw(account)
        elif choice == "4":
            print_statement(account)
        elif choice == "5":
            print("\n  Thank you for using the ATM. Goodbye!\n")
            break
        else:
            print("  [ERROR] Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
