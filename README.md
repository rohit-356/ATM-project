# ATM System

A simple menu-driven ATM system built in Python.

## Features

- **Display Balance** – View the current account balance.
- **Deposit Money** – Add funds to the account.
- **Withdraw Money** – Withdraw funds with insufficient-balance validation.
- **Account Statement** – View a record of all transactions.

## Project Structure

```
ATM-project/
├── main.py              # Entry point (menu loop)
├── atm_helpers.py       # Helper functions for ATM operations
├── README.md
└── .gitignore
```

## How to Run

```bash
python main.py
```

## Architecture

This project has been refactored to simplify the architecture:
- Removed the `Account` class in favor of passing variables (`balance`, `holder_name`, `transactions`).
- Flattened the directory structure by removing the `atm` package.
- Transactions are stored as plain readable strings without timestamps.
- **main.py** – Contains the menu loop and maintains the state variables.
- **atm_helpers.py** – Contains pure functions for menu display, getting input, deposits, withdrawals, and printing statements.
