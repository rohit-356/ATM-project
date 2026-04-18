"""
Display module — handles menu rendering and user input for navigation.
"""


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
