"""
Operations module — contains functions for each ATM operation.
All logic lives here; the main file only calls these functions.
"""


def display_balance(account):
    """Display the current account balance."""
    print("\n" + "=" * 40)
    print(f"  Account Holder : {account.holder_name}")
    print(f"  Current Balance: Rs.{account.get_balance():,.2f}")
    print("=" * 40)


def deposit(account):
    """Prompt the user for an amount and deposit it."""
    try:
        amount = float(input("\n  Enter amount to deposit: Rs."))
        if amount <= 0:
            print("  [ERROR] Amount must be greater than zero.")
            return
        account.credit(amount)
        print(f"  [SUCCESS] Rs.{amount:,.2f} deposited successfully.")
        print(f"  Updated Balance: Rs.{account.get_balance():,.2f}")
    except ValueError:
        print("  [ERROR] Invalid input. Please enter a numeric value.")


def withdraw(account):
    """Prompt the user for an amount and withdraw it."""
    try:
        amount = float(input("\n  Enter amount to withdraw: Rs."))
        if amount <= 0:
            print("  [ERROR] Amount must be greater than zero.")
            return
        if amount > account.get_balance():
            print("  [ERROR] Insufficient balance!")
            print(f"  Your current balance is Rs.{account.get_balance():,.2f}")
            return
        account.debit(amount)
        print(f"  [SUCCESS] Rs.{amount:,.2f} withdrawn successfully.")
        print(f"  Updated Balance: Rs.{account.get_balance():,.2f}")
    except ValueError:
        print("  [ERROR] Invalid input. Please enter a numeric value.")


def print_statement(account):
    """Print the full transaction statement."""
    transactions = account.get_transactions()

    print("\n" + "=" * 60)
    print(f"  ACCOUNT STATEMENT -- {account.holder_name}")
    print("=" * 60)

    if not transactions:
        print("  No transactions found.")
    else:
        print(f"  {'Date & Time':<22} {'Type':<18} {'Amount':>10} {'Balance':>10}")
        print("  " + "-" * 56)
        for txn in transactions:
            print(
                f"  {txn['date']:<22} {txn['type']:<18} "
                f"Rs.{txn['amount']:>9,.2f} Rs.{txn['balance']:>9,.2f}"
            )

    print("=" * 60)
