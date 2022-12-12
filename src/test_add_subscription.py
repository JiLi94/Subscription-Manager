import pytest
from subscription_handling import Subscription
from datetime import datetime

filepath = './src/data/subscription.json'
existing_subscriptions = Subscription(filepath)

# this test is designed to test the whole structure and data validations of the JSON file, to ensure all data are in correct formats.
def test_json_file_validation():
    # test whether the structure of the fila data is like: {[{},{}]}
    assert type(existing_subscriptions.file_data) is dict

    if not existing_subscriptions.is_empty():
        for category in list(existing_subscriptions.file_data.keys()):
            assert type(existing_subscriptions.file_data[category]) is list
            for item in existing_subscriptions.file_data[category]:
                assert type(item) is dict

    category_list = []
    subscription_name_list = []
    frequency_list = []
    charge_list = []
    date_list = []
    if not existing_subscriptions.is_empty():
        for category in list(existing_subscriptions.file_data.keys()):
            category_list.append(category.lower())
            for sub in existing_subscriptions.file_data[category]:
                subscription_name_list.append(sub['Name'].lower())
                charge_list.append(sub['Charge'])
                frequency_list.append(sub['Frequency'])
                date_list.append(sub['First bill date'])

        # test there are no duplicated categories (case insensitive)
        assert len(category_list) == len(set(category_list))

        # test there are no duplicated subscription names (case insensitive)
        assert len(subscription_name_list) == len(set(subscription_name_list))

        # test all charges of the subscriptions are floats
        for charge in charge_list:
            assert type(charge) is float

        # test all frequency fields of the subscriptions are in the list ['Daily', 'Monthly', 'Quarterly', 'Annual']
        for frequency in frequency_list:
            assert frequency in existing_subscriptions.frequency_option

        # test all dates in the 'First bill date' fields are in valid date formats
        for date in date_list:
            try:
                date_converted = datetime.strptime(date, '%Y-%m-%d').date()
            except:
                assert False
