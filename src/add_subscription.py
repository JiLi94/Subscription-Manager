from json_handling import read_json, write_json, delete_json
from terminal_menu import terminal_menu
import json


class Subscription():

    def __init__(self, filepath='./src/subscription.json'):
        self.filepath = filepath

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
        elif mode == 'update':
            pass

        return category_list

    def select_category(self, mode):
        # get category list based on different mode
        category_option = self.category_list(mode)
        prompt = 'Please select a category of the subscription:'
        # get user to select category
        category_selected = terminal_menu(category_option, prompt)
        # if user would like to add new category, ask for new category name
        if category_selected == 'Add New Category':
            category_selected = input(
                'Please enter the name of the new category: ')

        return category_selected

    def select_subscription(self, category):
        file_data = read_json(self.filepath)
        subscription_list = file_data[category]

        # ask user to select name of the subscription
        prompt = 'Please select one subscription to update:'
        subscription_name_selected = terminal_menu(
            [sub['Name'] for sub in subscription_list], prompt)

        # get the dictionary with corresponding name
        for i in subscription_list:
            if i['Name'] == subscription_name_selected:
                subscription_selected = i
                break

        return subscription_selected

    def view_subscription(self):
        file_data = read_json(self.filepath)
        category_selected = self.select_category(mode='view')

        # print the subscriptions
        if category_selected == 'View All':
            print(json.dumps(file_data, indent=4))
        else:
            print(json.dumps(file_data[category_selected], indent=4))

    def input_name(self):
        # get names of existing subscriptions
        file_data = read_json(self.filepath)
        existing_subscription = []
        for category in file_data:
            for subscription in file_data[category]:
                existing_subscription.append(subscription['Name'])

        # ask for name of the subscription
        name = input('Please enter the name of the subscription: ')
        # avoid duplicates
        while name.lower() in [sub.lower() for sub in existing_subscription]:
            name = input(
                'Name exists! Please enter a different name: ')

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
        # ask user to select a category first
        category_selected = self.select_category(mode='update')
        # ask user to select a subscription
        subscription_selected = self.select_subscription(category_selected)
        # delete the selected subscription first, then can add back the updated one
        delete_json(category_selected, subscription_selected, self.filepath)

        prompt = 'Please select the attribute you would like to update:'
        # turn the dict into a list so it can be passed into the terminal_menu function
        option_list = ['Category'+ ': ' + category_selected]
        for key, value in subscription_selected.items():
            option_list.append(str(key) + ': ' + str(value))

        selected_attribute = terminal_menu(option_list, prompt)

        # update the subscription based on user's input
        if 'Category: ' in selected_attribute:
            category_selected = self.select_category(mode = 'add')
        if 'Name: ' in selected_attribute:
            subscription_selected['Name'] = self.input_name()
        if 'Frequency: ' in selected_attribute:
            subscription_selected['Frequency'] = self.select_frequency()
        if 'Charge: ' in selected_attribute:
            subscription_selected['Charge'] = self.input_charge()
        # write the updated subscription into database
        write_json(category_selected, subscription_selected, self.filepath)


new_sub = Subscription()
# new_sub.input_name()
# new_sub.category_list(mode='add')
# new_sub.add_subscription()
# new_sub.view_subscription()

new_sub.update_subscription()
# new_sub.select_subscription('Utility')
