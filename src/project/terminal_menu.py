from simple_term_menu import TerminalMenu


def terminal_menu(options, prompt):
    print(prompt)
    while True:
        try:
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            selected = options[menu_entry_index]
            print(selected)
            return selected
            break
        # error handling when user inputs invalid value, instead of selecting one option from the menu
        except TypeError:
            print('Please select one option from of the menu')
