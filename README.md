# ATM System

A simple menu-driven ATM system built in Python using package architecture.

## Features

- **Display Balance** – View the current account balance.
- **Deposit Money** – Add funds to the account.
- **Withdraw Money** – Withdraw funds with insufficient-balance validation.
- **Account Statement** – View a timestamped record of all transactions.

## Project Structure

```
atm_system/
├── main.py              # Entry point (menu loop, no business logic)
├── README.md
├── .gitignore
└── atm/                 # Package containing all logic
    ├── __init__.py      # Public API exports
    ├── account.py       # Account class (balance + transaction history)
    ├── operations.py    # Deposit, withdraw, balance, statement functions
    └── display.py       # Menu rendering and user input
```

## How to Run

```bash
python main.py
```

## Architecture

- **main.py** – Contains only the menu loop and delegates all operations to the `atm` package.
- **atm/account.py** – `Account` class that manages balance and records every transaction with a timestamp.
- **atm/operations.py** – Functions for deposit, withdrawal, balance display, and statement printing.
- **atm/display.py** – Menu display and user input handling.
