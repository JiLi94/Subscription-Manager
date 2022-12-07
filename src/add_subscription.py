import json
from terminal_manual import terminal_menu_frequency, terminal_menu_category


def write_json(category, subscription_detail, filename='./src/subscription.json'):
    with open(filename, 'r') as file:
        file_data = json.load(file)

        # if category exists, add new data into the category
        if category in file_data:
            file_data[category].append(subscription_detail)
        else:
            pass  # if new category, use dict.update??
        # file_data.update(new_data)
    
    with open(filename, 'w') as file:
        json.dump(file_data, file)


def add_subscription():
    # ask for category
    print('Please select a category of the subscription or add a new category')
    category = terminal_menu_category()
    print(category)

    # ask for name of the subscription
    name = input('Please enter the name of the subscription: ')

    # ask for frequency of the subscription
    print('Please select the frequency of subscription:')
    frequency = terminal_menu_frequency()
    print(frequency)

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
        'Frequency': frequency,
        'Charge': charge
    }

    # add new subscription to the list using the function write_json
    write_json(category, new_subscription)


add_subscription()


# def write_json(new_data, filename = 'subscription.json')

# with open('./src/subscription.json', 'w') as file:
#     json.dump(add_subscription(), file)
