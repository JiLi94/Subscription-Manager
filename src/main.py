from subscription_handling import Subscription
from getkey import getkey, key

filepath = './src/data/subscription.json'
subscription = Subscription(filepath)


def dash_line():
    print('-'*100)


while True:
    dash_line()
    selection = subscription.view_main_menu()

    match selection:
        case 'View existing subscriptions':
            dash_line()
            subscription.view_subscription()
        case 'Update existing subscriptions':
            dash_line()
            subscription.update_subscription()
        case 'Delete existing subscriptions':
            dash_line()
            subscription.delete_subscription()
        case 'Calculate my cost':
            dash_line()
            subscription.cost()
        case 'Exit':
            print('Goodbye!')
            break

    dash_line()
    print('Press ENTER to go back to the main menu, or press anything else to exit the application')
    user_input = getkey()

    if user_input == key.ENTER:
        continue
    else:
        print('Goodbye!')
        break
