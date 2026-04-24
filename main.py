from atm_helpers import show_menu, get_choice, display_balance, deposit, withdraw, print_statement

def main():
    print("\n  Welcome to the ATM System!")
    holder_name = input("  Enter account holder name: ").strip()

    # Create an account with an optional opening balance
    try:
        balance = float(input("  Enter opening balance: Rs."))
    except ValueError:
        balance = 0

    transactions = []
    if balance > 0:
        transactions.append(f"OPENING BALANCE: Rs.{balance:,.2f} | Balance: Rs.{balance:,.2f}")

    print(f"\n  [SUCCESS] Account created for {holder_name} with balance Rs.{balance:,.2f}")

    # ---- Infinite loop menu system ----
    while True:
        show_menu()
        choice = get_choice()

        if choice == "1":
            display_balance(holder_name, balance)
        elif choice == "2":
            balance = deposit(balance, transactions)
        elif choice == "3":
            balance = withdraw(balance, transactions)
        elif choice == "4":
            print_statement(holder_name, transactions)
        elif choice == "5":
            print("\n  Thank you for using the ATM. Goodbye!\n")
            break
        else:
            print("  [ERROR] Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
