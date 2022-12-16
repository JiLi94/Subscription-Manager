from json_handling import *
from terminal_menu import terminal_menu
from datetime import datetime
import json


class Subscription():

    def __init__(self, filepath):
        self.filepath = filepath
        self.frequency_option = ["Daily", "Monthly", "Quarterly", "Annual"]
        self.default_category = ['Entertainment', 'Productivity', 'Utility']
        self.file_data = read_json(self.filepath)
        self.main_menu = ['View existing subscriptions', 'Update existing subscriptions',
                          'Delete existing subscriptions', 'Calculate my cost', 'Exit']

    def is_empty(self):
        if self.file_data == {}:
            return True
        else:
            return False

    def view_main_menu(self):
        prompt = 'Welcome to your subscription manager, please select one option from the menu'
        return terminal_menu(self.main_menu, prompt)

    def category_list(self, mode):
        # read JSON file and get the list of category
        category_list = list(self.file_data.keys())

        # when view subscriptions, add an option to view all
        if mode == 'view':
            category_list.insert(0, 'View All')
        # when add subscriptions, show all existing categories and anything left in the default category
        elif mode == 'add':
            category_list = list(
                set(category_list).union(set(self.default_category)))
            # sort the category list alphabetically
            category_list = sorted(category_list)
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
                'Please enter the name of the new category: ').strip()
            # data validation, when input is empty
            while category_selected == '':
                category_selected = input(
                    'Please enter a valid category name: ').strip()

            # avoid duplicates
            for category in category_option:
                if category_selected.lower() == category.lower():
                    category_selected = category
                    break

        return category_selected

    def select_subscription(self, category):
        subscription_list = self.file_data[category]

        # ask user to select name of the subscription
        prompt = 'Please select one subscription:'
        subscription_name_selected = terminal_menu(
            [sub['Name'] for sub in subscription_list], prompt)

        # get the dictionary with corresponding name
        for i in subscription_list:
            if i['Name'] == subscription_name_selected:
                subscription_selected = i
                break

        return subscription_selected

    def view_subscription(self):
        if self.is_empty():
            print('You don\'t have any existing subscriptions')
        else:
            self.file_data = read_json(self.filepath)
            category_selected = self.select_category(mode='view')

            if category_selected == 'View All':
                print_json(self.file_data, 4)
            else:
                print_json(self.file_data[category_selected], 4)

    def input_name(self):
        # get names of existing subscriptions
        existing_subscription = []
        for category in self.file_data:
            for subscription in self.file_data[category]:
                existing_subscription.append(subscription['Name'])

        # ask for name of the subscription
        name = input('Please enter the name of the subscription: ').strip()

        while True:
            # data validation, when input is empty
            if name == '':
                name = input('Please enter a valid name: ')
            # avoid duplicates
            elif name.lower().strip() in [sub.lower() for sub in existing_subscription]:
                name = input(
                    'Subscription exists! Please enter a different name: ').strip()
            else:
                break

        return name

    def select_frequency(self):
        # ask for frequency of the subscription
        prompt = 'Please select the frequency:'
        frequency_selected = terminal_menu(self.frequency_option, prompt)
        return frequency_selected

    def input_charge(self):
        # ask for charge of the subscription
        while True:
            try:
                charge = float(
                    input('Please enter the charge of the subscription: '))
                if charge < 0:
                    print('Please enter a positive number!')
                    continue
            # if user doesn't enter a valid number, ask again
            except ValueError:
                print('Please enter a valid number!')
                continue
            else:
                break

        return charge

    def input_date(self):
        user_input = input(
            'Please enter the date of the first bill in the format of yyyy-mm-dd: ')
        while True:
            # error handling, when user didn't input a valid date
            try:
                first_bill_date = datetime.strptime(
                    user_input, '%Y-%m-%d').date()
                break
            except ValueError:
                user_input = input(
                    'Please enter a valid date in the format of yyyy-mm-dd: ')
                continue
            else:
                break

        return str(first_bill_date)

    def add_subscription(self):
        # ask user to select/input attributes
        category_selected = self.select_category(mode='add')
        name = self.input_name()
        frequency_selected = self.select_frequency()
        charge = self.input_charge()
        first_bill_date = self.input_date()

        new_subscription = {
            'Name': name,
            'Frequency': frequency_selected,
            'Charge': charge,
            'First bill date': first_bill_date
        }

        print(new_subscription)
        # add new subscription to the list using the function write_json
        write_json(category_selected, new_subscription, self.filepath)
        return [category_selected, new_subscription]

    def delete_subscription(self):
        if self.is_empty():
            print('You don\'t have any existing subscriptions')
        else:
            # ask user to select a category and subscription first
            category_selected = self.select_category(mode='update')
            subscription_selected = self.select_subscription(category_selected)
            confirmation = input(
                f'Are you sure to delete {subscription_selected}? Input Yes/No to confirm: ')
            while True:
                if confirmation.lower() == 'yes':
                    delete_json(category_selected,
                                subscription_selected, self.filepath)
                    print('Deleted successfully!')
                    break
                elif confirmation.lower() == 'no':
                    break
                else:
                    confirmation = input(
                        'Please enter "Yes" or "No" to confirm: ')

    def update_subscription(self):
        if self.is_empty():
            print('You don\'t have any existing subscriptions')
        else:
            # ask user to select a category and subscription first
            category_selected = self.select_category(mode='update')
            subscription_selected = self.select_subscription(category_selected)

            # assign category and subscription to another variable
            category_selected_updated = category_selected
            subscription_selected_updated = subscription_selected.copy()

            # keep asking user to update attributes unless user selects 'Done'
            while True:
                # turn the dict into a list so it can be passed into the terminal_menu function
                option_list = ['Category' + ': ' + category_selected_updated]
                for key, value in subscription_selected_updated.items():
                    option_list.append(str(key) + ': ' + str(value))

                option_list.append('Done')

                prompt = 'Please select the attribute you would like to update or select \'Done\' after finish:'
                # get what attribute of the subscription the user has selected, possible output: Category, Name, Frequency, Charge, First bill data
                selected_attribute = terminal_menu(
                    option_list, prompt).split(':')[0]

                # update the subscription based on user's selection
                match selected_attribute:
                    case 'Category':
                        category_selected_updated = self.select_category(
                            mode='add')
                    case 'Name':
                        subscription_selected_updated['Name'] = self.input_name(
                        )
                    case 'Frequency':
                        subscription_selected_updated['Frequency'] = self.select_frequency(
                        )
                    case 'Charge':
                        subscription_selected_updated['Charge'] = self.input_charge(
                        )
                    case 'First bill date':
                        subscription_selected_updated['First bill date'] = self.input_date(
                        )

                # user finishes updating
                if selected_attribute == 'Done':
                    break

            # delete original subscription
            delete_json(category_selected,
                        subscription_selected, self.filepath)
            # write the updated subscription into database
            write_json(category_selected_updated,
                       subscription_selected_updated, self.filepath)
            # print the updated record
            print_json(subscription_selected_updated, 4)

    def cost(self):
        frequency_selected = self.select_frequency()

        # file_data = read_json(self.filepath)
        # calculate total cost of each frequency
        cost_dict = {}
        for frequency in self.frequency_option:
            cost = 0
            for category in self.file_data:
                for sub in self.file_data[category]:
                    # print(sub)
                    if sub['Frequency'] == frequency:
                        cost += sub['Charge']
            cost_dict[frequency] = cost

        # calculate the estimated cost for each frequency
        cost_daily = cost_dict['Daily'] + cost_dict['Monthly'] * 12 / \
            365 + cost_dict['Quarterly'] * 4 / 365 + cost_dict['Annual'] / 365
        cost_monthly = cost_dict['Daily'] * 365 / 12 + cost_dict['Monthly'] + \
            cost_dict['Quarterly'] / 3 + cost_dict['Annual'] / 12
        cost_quarterly = cost_dict['Daily'] * 365 / 4 + cost_dict['Monthly'] * \
            3 + cost_dict['Quarterly'] + cost_dict['Annual'] / 4
        cost_annual = cost_dict['Daily'] * 365 + cost_dict['Monthly'] * \
            12 + cost_dict['Quarterly'] * 4 + cost_dict['Annual']

        cost_dict['Daily'] = cost_daily
        cost_dict['Monthly'] = cost_monthly
        cost_dict['Quarterly'] = cost_quarterly
        cost_dict['Annual'] = cost_annual

        # print results
        print(
            f'Based on your subscriptions, your estimated {frequency_selected.lower()} cost is ${round(cost_dict[frequency_selected],2)}')


# new_sub = Subscription('./src/data/subscription.json')
# new_sub.input_name()
# new_sub.category_list(mode='add')
# new_sub.add_subscription()
# new_sub.view_subscription()

# new_sub.update_subscription()
# new_sub.select_subscription('Utility')
# new_sub.delete_subscription()
# print(new_sub.is_empty())
# new_sub.cost()
# print(new_sub.view_main_menu())
