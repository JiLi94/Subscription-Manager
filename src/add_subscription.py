from json_handling import print_json, write_json
from terminal_menu import Menu


class Subscription():

    def __init__(self, filename='./src/subscription.json'):
        self.filename = filename

    def view_subscription(self):
        print_json()

    def add_subscription(self):
        # ask for category
        category_option = ["Entertainment",
                           "Productivity", "Utility", "Add New Category"]
        category_menu = Menu(category_option)
        print('Please select a category of the subscription: ')
        category_selected = category_menu.print_menu()
        print(category_selected)

        # ask for name of the subscription
        name = input('Please enter the name of the subscription: ')

        # ask for frequency of the subscription
        frequency_option = ["Daily", "Monthly", "Quarterly", "Annual"]
        frequency_menu = Menu(frequency_option)
        print('Please select the frequency of subscription:')
        frequency_selected = frequency_menu.print_menu()
        print(frequency_selected)

        # ask for charge of the subscription
        while True:
            try:
                charge = float(
                    input('Please enter the charge of the subscription: '))
            # if user doesn't enter a correct number, ask again
            except ValueError:
                print('Please enter a valid number!')
                continue
            else:
                break

        new_subscription = {
            'Name': name,
            'Frequency': frequency_selected,
            'Charge': charge
        }

        # add new subscription to the list using the function write_json
        write_json(category_selected, new_subscription)


new_sub = Subscription()
new_sub.add_subscription()
new_sub.view_subscription()
