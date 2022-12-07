from simple_term_menu import TerminalMenu


def terminal_menu():
    options = ["View All Subscriptions", "Add New Subscription", "Add New Category", "View My Total Cost"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")

terminal_menu()