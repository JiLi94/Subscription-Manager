from simple_term_menu import TerminalMenu


def terminal_menu_main():
    options = ["View All Subscriptions", "Add New Subscription",
               "Add New Category", "View My Total Cost"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")


def terminal_menu_frequency():
    options = ["Daily", "Monthly", "Quarterly", "Annual"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    return options[menu_entry_index]
    # print(f"You have selected {options[menu_entry_index]}!")


def terminal_menu_category():
    options = ["Entertainment", "Productivity", "Utility", "Add New Category"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    return options[menu_entry_index]
# terminal_menu()
