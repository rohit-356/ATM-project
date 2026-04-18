"""
Account module — holds the Account class that manages
balance and transaction history.
"""

from datetime import datetime


class Account:
    """Represents a bank account with balance and transaction history."""

    def __init__(self, holder_name, initial_balance=0):
        self.holder_name = holder_name
        self.balance = initial_balance
        self.transactions = []

        # Record the opening balance as the first transaction
        if initial_balance > 0:
            self._record("OPENING BALANCE", initial_balance)

    # ---- internal helper ----
    def _record(self, txn_type, amount):
        """Append a transaction record with timestamp."""
        self.transactions.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": txn_type,
            "amount": amount,
            "balance": self.balance,
        })

    # ---- public methods ----
    def credit(self, amount):
        """Add money to the account."""
        self.balance += amount
        self._record("DEPOSIT", amount)

    def debit(self, amount):
        """Remove money from the account (caller must validate first)."""
        self.balance -= amount
        self._record("WITHDRAWAL", amount)

    def get_balance(self):
        """Return the current balance."""
        return self.balance

    def get_transactions(self):
        """Return the full transaction history."""
        return self.transactions
