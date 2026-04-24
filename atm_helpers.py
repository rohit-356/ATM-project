def show_menu():
    """Print the ATM main menu."""
    print("\n" + "╔" + "═" * 38 + "╗")
    print("║" + "  ATM SYSTEM  ".center(38) + "║")
    print("╠" + "═" * 38 + "╣")
    print("║  1. Display Balance                 ║")
    print("║  2. Deposit Money                   ║")
    print("║  3. Withdraw Money                  ║")
    print("║  4. Account Statement               ║")
    print("║  5. Exit                            ║")
    print("╚" + "═" * 38 + "╝")

def get_choice():
    """Get and return the user's menu choice."""
    choice = input("  Enter your choice (1-5): ").strip()
    return choice

def display_balance(holder_name, balance):
    """Display the current account balance."""
    print("\n" + "=" * 40)
    print(f"  Account Holder : {holder_name}")
    print(f"  Current Balance: Rs.{balance:,.2f}")
    print("=" * 40)

def deposit(balance, transactions):
    """Prompt the user for an amount and deposit it."""
    try:
        amount = float(input("\n  Enter amount to deposit: Rs."))
        if amount <= 0:
            print("  [ERROR] Amount must be greater than zero.")
            return balance
        balance += amount
        transactions.append(f"DEPOSIT: Rs.{amount:,.2f} | Balance: Rs.{balance:,.2f}")
        print(f"  [SUCCESS] Rs.{amount:,.2f} deposited successfully.")
        print(f"  Updated Balance: Rs.{balance:,.2f}")
        return balance
    except ValueError:
        print("  [ERROR] Invalid input. Please enter a numeric value.")
        return balance

def withdraw(balance, transactions):
    """Prompt the user for an amount and withdraw it."""
    try:
        amount = float(input("\n  Enter amount to withdraw: Rs."))
        if amount <= 0:
            print("  [ERROR] Amount must be greater than zero.")
            return balance
        if amount > balance:
            print("  [ERROR] Insufficient balance!")
            print(f"  Your current balance is Rs.{balance:,.2f}")
            return balance
        balance -= amount
        transactions.append(f"WITHDRAWAL: Rs.{amount:,.2f} | Balance: Rs.{balance:,.2f}")
        print(f"  [SUCCESS] Rs.{amount:,.2f} withdrawn successfully.")
        print(f"  Updated Balance: Rs.{balance:,.2f}")
        return balance
    except ValueError:
        print("  [ERROR] Invalid input. Please enter a numeric value.")
        return balance

def print_statement(holder_name, transactions):
    """Print the full transaction statement."""
    print("\n" + "=" * 60)
    print(f"  ACCOUNT STATEMENT -- {holder_name}")
    print("=" * 60)

    if not transactions:
        print("  No transactions found.")
    else:
        for txn in transactions:
            print(f"  {txn}")

    print("=" * 60)
