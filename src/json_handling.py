import json


def print_json(filename='./src/subscription.json'):
    with open(filename, 'r') as file:
        file_data = json.load(file)
        print(json.dumps(file_data, indent=2)) #pretty print JSON


def write_json(category, subscription_detail, filename='./src/subscription.json'):
    with open(filename, 'r') as file:
        file_data = json.load(file)

        # if category exists, add new data into the category
        if category in file_data:
            file_data[category].append(subscription_detail)
        # else add a new category
        else:
            file_data.update({category: subscription_detail})
        # file_data.update(new_data)

    with open(filename, 'w') as file:
        json.dump(file_data, file)
