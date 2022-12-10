import json


def read_json(filepath):
    with open(filepath, 'r') as file:
        file_data = json.load(file)
        # print(json.dumps(file_data, indent=2))  # pretty print JSON

    return file_data


def write_json(category, subscription, filepath):
    file_data = read_json(filepath)

    # if has subscription exists under the category, add new data into the category
    if category in file_data:
        # print(file_data[category])
        file_data[category].append(subscription)

    # if no subscription exists under the category, add the category
    else:
        file_data.update({category: [subscription]})
    # file_data.update(new_data)

    with open(filepath, 'w') as file:
        json.dump(file_data, file)

    print('Updated Successfully!')


def delete_json(category, subscription, filepath):
    file_data = read_json(filepath)
    file_data[category].remove(subscription)

    with open(filepath, 'w') as file:
        json.dump(file_data, file)

# file_data = read_json('./src/subscription.json')
# print(str(file_data['Utility']))
# new_list = []
# for i in file_data['Utility']:
#     new_list.append(str(i))

# print(new_list)
