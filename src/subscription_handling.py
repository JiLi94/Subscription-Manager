from json_handling import read_json, write_json, delete_json
from terminal_menu import terminal_menu
from datetime import datetime
import json


class Subscription():

    def __init__(self, filepath='./src/subscription.json'):
        self.filepath = filepath
        self.frequency_option = ["Daily", "Monthly", "Quarterly", "Annual"]
        self.default_category = ['Entertainment', 'Productivity', 'Utility']

    def is_empty(self):
        file_data = read_json(self.filepath)
        if file_data == {}:
            return True
        else:
            return False

    def category_list(self, mode):
        file_data = read_json(self.filepath)
        # read JSON file and get the list of category
        category_list = list(file_data.keys())

        # when view subscriptions, add an option to view all
        if mode == 'view':
            category_list.insert(0, 'View All')
        # when add subscriptions, show all existing categories and anything left in the default category
        elif mode == 'add':

            category_list = list(
                set(category_list).union(set(self.default_category)))
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
        file_data = read_json(self.filepath)
        category_selected = self.select_category(mode='view')

        # print the subscriptions
        if self.is_empty():
            print('You don\'t have any existing subscriptions')
        elif category_selected == 'View All':
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
                'Subscription exists! Please enter a different name: ')

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
            # if user doesn't enter a correct number, ask again
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
                first_bill_date = datetime.strptime(user_input, '%Y-%m-%d').date()
                break
            except ValueError:
                user_input = input('Please enter a valid date in the format of yyyy-mm-dd: ')
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

    def delete_subscription(self, mode='delete'):
        if self.is_empty():
            print('You don\'t have any existing subscriptions')
        else:
            # ask user to select a category first
            category_selected = self.select_category(mode='update')
            # ask user to select a subscription
            subscription_selected = self.select_subscription(category_selected)
            # delete the selected subscription
            # if user selects to delete, add a confirmation before deleting
            if mode == 'delete':
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
            # if mode is not 'delete', no confirmation needed, because it will be added back later with updated info
            else:
                delete_json(category_selected,
                            subscription_selected, self.filepath)

            return [category_selected, subscription_selected]

    def update_subscription(self):
        if self.is_empty():
            print('You don\'t have any existing subscriptions')
        else:
            # delete the selected subscription first, then can add back the updated one
            selected = self.delete_subscription(mode='update')

            prompt = 'Please select the attribute you would like to update:'
            # turn the dict into a list so it can be passed into the terminal_menu function
            option_list = ['Category' + ': ' + selected[0]]
            for key, value in selected[1].items():
                option_list.append(str(key) + ': ' + str(value))

            selected_attribute = terminal_menu(option_list, prompt)

            # update the subscription based on user's selection
            if 'Category: ' in selected_attribute:
                selected[0] = self.select_category(mode='add')
            if 'Name: ' in selected_attribute:
                selected[1]['Name'] = self.input_name()
            if 'Frequency: ' in selected_attribute:
                selected[1]['Frequency'] = self.select_frequency()
            if 'Charge: ' in selected_attribute:
                selected[1]['Charge'] = self.input_charge()
            if 'First bill date: ' in selected_attribute:
                selected[1]['First bill date'] = self.input_date()
            # write the updated subscription into database
            write_json(selected[0], selected[1], self.filepath)

    def cost(self):
        frequency_selected = self.select_frequency()

        file_data = read_json(self.filepath)
        # calculate total cost of each frequency
        cost_dict = {}
        for frequency in self.frequency_option:
            cost = 0
            for category in file_data:
                for sub in file_data[category]:
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

        match frequency_selected:
            case 'Daily':
                print(
                    f'Based on your subscriptions, your estimated daily cost is ${round(cost_daily,2)}')
            case 'Monthly':
                print(
                    f'Based on your subscriptions, your estimated monthly cost is ${round(cost_monthly,2)}')
            case 'Quarterly':
                print(
                    f'Based on your subscriptions, your estimated quarterly cost is ${round(cost_quarterly,2)}')
            case 'Annual':
                print(
                    f'Based on your subscriptions, your estimated annual cost is ${round(cost_annual,2)}')


new_sub = Subscription()
# new_sub.input_name()
# new_sub.category_list(mode='add')
# new_sub.add_subscription()
# new_sub.view_subscription()

# new_sub.update_subscription()
# new_sub.select_subscription('Utility')
new_sub.delete_subscription()
# print(new_sub.is_empty())
# new_sub.cost()
