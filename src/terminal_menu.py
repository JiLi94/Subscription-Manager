from simple_term_menu import TerminalMenu


# define Terminal_menu class
class Menu():

    def __init__(self, option):
        self.option = option

    def print_menu(self):
        terminal_menu = TerminalMenu(self.option)
        menu_entry_index = terminal_menu.show()
        return self.option[menu_entry_index]


# main_menu = ["View All Subscriptions", "Add New Subscription",
#              "Add New Category", "View My Total Cost"]
# frequency = ["Daily", "Monthly", "Quarterly", "Annual"]
# category = ["Entertainment", "Productivity", "Utility", "Add New Category"]
# menu = Menu(main_menu)
# print(menu.print_menu())
