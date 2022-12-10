from simple_term_menu import TerminalMenu

def terminal_menu(option, prompt):
    print(prompt)
    terminal_menu = TerminalMenu(option)
    menu_entry_index = terminal_menu.show()
    selected = option[menu_entry_index]
    print(selected)
    return selected


# main_menu = ["View All Subscriptions", "Add New Subscription",
#              "Add New Category", "View My Total Cost"]
# frequency = ["Daily", "Monthly", "Quarterly", "Annual"]
# category = ["Entertainment", "Productivity", "Utility", "Add New Category"]
# menu = Menu(main_menu)
# print(menu.print_menu())
