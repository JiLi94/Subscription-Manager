from json_handling import read_json, write_json
from terminal_menu import terminal_menu
import json


class Subscription():

    def __init__(self, filepath='./src/subscription.json'):
        self.filepath = filepath

    # def file_data(self):
    #     with open(self.filepath, 'r') as file:
    #         file_data = json.load(file)

    #     return file_data

    def category_list(self, mode):
        file_data = read_json(self.filepath)
        # read JSON file and get the list of category
        category_list = list(file_data.keys())

        # when view subscriptions, add an option to view all
        if mode == 'view':
            category_list.insert(0, 'View All')
        # when add subscriptions, show all existing categories and anything left in the default category
        elif mode == 'add':
            default_category = ['Entertainment', 'Productivity', 'Utility']
            category_list = list(
                set(category_list).union(set(default_category)))
            category_list.append('Add New Category')

        return category_list

    def select_category(self, mode):
        # get category list based on different mode
        category_option = self.category_list(mode)

        if mode == 'view':
            prompt = 'To view current subscriptions, please select a category:'
        elif mode == 'add':
            prompt = 'To add new subscription, please select a category of the subscription:'

        # get user to select category
        category_selected = terminal_menu(category_option, prompt)
        # if user would like to add new category, ask for new category name
        if category_selected == 'Add New Category':
            category_selected = input(
                'Please enter the name of the new category: ')

        return category_selected

    def view_subscription(self):
        file_data = read_json(self.filepath)
        category_selected = self.select_category(mode='view')

        # print the subscriptions
        if category_selected == 'View All':
            print(json.dumps(file_data, indent=4))
        else:
            print(json.dumps(file_data[category_selected], indent=4))

    def input_name(self):
        # ask for name of the subscription
        name = input('Please enter the name of the subscription: ')
        return name

    def select_frequency(self):
        # ask for frequency of the subscription
        frequency_option = ["Daily", "Monthly", "Quarterly", "Annual"]
        prompt = 'Please select the frequency of subscription:'
        frequency_selected = terminal_menu(frequency_option, prompt)
        return frequency_selected

    def input_charge(self):
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

        return charge

    def add_subscription(self):
        category_selected = self.select_category(mode='add')
        name = self.input_name()
        frequency_selected = self.select_frequency()
        charge = self.input_charge()

        new_subscription = {
            'Name': name,
            'Frequency': frequency_selected,
            'Charge': charge
        }

        print(new_subscription)
        # add new subscription to the list using the function write_json
        write_json(category_selected, new_subscription, self.filepath)

    def update_subscription(self):
        # print existing categories for user to select
        category_menu = Menu(self.existing_category())
        print('To update existing subscription, please select a category of the subscription: ')
        category_selected = category_menu.print_menu()
        print(category_selected)

        # ask for user to select one subscription to update
        print('Please select one subscription to update:')
        with open(self.filepath, 'r') as file:
            file_data = json.load(file)

        list_of_sub = file_data[category_selected]
        subscription_menu = Menu([sub['Name'] for sub in list_of_sub])
        subscription_selected = subscription_menu.print_menu()
        print(subscription_selected)


new_sub = Subscription()
# new_sub.category_list(mode='add')
new_sub.add_subscription()
# new_sub.view_subscription()

# new_sub.update_subscription()
