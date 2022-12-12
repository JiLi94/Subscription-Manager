from subscription_handling import Subscription
def add_sub():
    add_sub = Subscription(filepath = './src/test_data.json')
    new_sub = add_sub.add_subscription()
    return new_sub