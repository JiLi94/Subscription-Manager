from json_handling import write_json
from terminal_menu import Menu
import json


class Subscription():

    def __init__(self, filename='./src/subscription.json'):
        self.filename = filename

    def view_subscription(self):
        with open(self.filename, 'r') as file:
            file_data = json.load(file)

            # get the categories of existing subscriptions
            category_option = list(file_data.keys())
            category_option.insert(0, 'View All')

            # prompt a terminal menu to ask for user to select a category
            category_menu = Menu(category_option)
            print('To view current subscriptions, please select a category:')
            category_selected = category_menu.print_menu()
            print(category_selected)

            # print the subscriptions
            if category_selected == 'View All':
                print(json.dumps(file_data, indent=4))
            else:
                print(json.dumps(file_data[category_selected], indent=2))

    def add_subscription(self):
        category_option = ['Entertainment', 'Productivity', 'Utility']

        with open(self.filename, 'r') as file:
            file_data = json.load(file)
            # get the categories of existing subscriptions
            for option in list(file_data.keys()):
                if option not in category_option:
                    category_option.append(option)

            category_option.append('Add New Category')

        category_menu = Menu(category_option)
        print('To add new subscription, please select a category of the subscription: ')
        category_selected = category_menu.print_menu()

        # if user would like to add new category, ask for new category name
        if category_selected == 'Add New Category':
            category_selected = input(
                'Please enter the name of the new category: ')
        else:
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
        write_json(category_selected, new_subscription, self.filename)


new_sub = Subscription()
# new_sub.add_subscription()
new_sub.view_subscription()
