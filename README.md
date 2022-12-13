# JiLi_T1A3 Terminal App - Subscription Manager

## GitHub repo

[JiLi_T1A3 - Subscription Manager](https://github.com/JiLi94/Subscription-Manager.git)

## Presentation video

## Project description

This project aims to help the user to create and manage their own subscription lists. The features include view current subscription list, create new subscription, update/delete existing subscriptions and calculate the cost based on their frequencies.

https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/#:~:text=In%20simple%20words%2C%20we%20can,install%20and%20run%20the%20project.

## How to install and run this project

## Features

## Testing

### JSON data validation

This test was designed to be an automation test. The idea is to test the whole structure of the JSON file and validate the data inside it. For example:

- The application was designed to not have duplicated categories or subscription names

- The 'frequency' of the subscriptions are not customizable and can only be one of ['Daily', 'Monthly', 'Quarterly', 'Annual']

- The 'charge' of the subscriptions should be floats

- The 'first bill date' of the subscriptions should be in the format of 'yyyy-mm-dd'

These test cases ensure the features such as add new or update existing subscriptions to write correct data into the database.

### Testing the feature of deleting existing subscriptions

This test was designed to test if the feature of deleting existing items works as expected. This test requires human input and due to time limit, it's not been automated. Manual test procedures are outlined below.

1. Select 'view existing subscriptions' to check the existing categories

    ![view category](docs/test/view-category.png)

2. Exit and select 'delete existing subscriptions', the terminal menu should be showing the same categories with step 1 (excluding 'View All')

    ![delete category](docs/test/delete-category.png)

3. If there is no existing subscription, the terminal menu should be showing 'You don't have any existing subscriptions'

4. Select into one category and select one subscription, the terminal menu should be confirming if the user really intends to delete the record
    
    ![delete confirmation](docs/test/delete-confirmation.png)

5. The delete confirmation only accepts 'Yes' or 'No' as the answer. If user input is not 'Yes' or 'No', the user will be asked again until correct answer is received
    
    ![delete confirmation 2](docs/test/delete-confirmation-2.png)

6. If user inputs 'No', the application stops and nothing gets deleted. If user inputs 'Yes', the selected record will be deleted and users will be informed as 'deleted successfully'.

7. After deleting successfully, if user selects to view the existing subscription again, the record should not exist. If no subscription exists under a certain category, the category should be deleted as well, so the user cannot view the category either.

## Limitations and future expectations

- terminal menu can be more sophisticated, such as add preview window, allow multiple choice

- allow reverse actions

- can allow to add more contents to each subscription in the future, such as website url, etc. 

- This application only supports single user for now, but in the future hopefully it will be implemented more features so it can allow multiple users to create their own lists, and they can log in with their username and passwords.

## References

- Packages & modules:

    - For showing menus in terminal for user to select: [simple terminal menu package](https://pypi.org/project/simple-term-menu/)

    - For manipulating JSON files: [json](https://docs.python.org/3/library/json.html)

    - For conversion between strings and datetime: [datetime](https://docs.python.org/3/library/datetime.html)

    - For get keyboard input from the user: [getkey](https://pypi.org/project/getkey/)

    - For testing: [pytest](https://docs.pytest.org/en/7.2.x/getting-started.html)

    - For tools to deal with filepath and directories: [sys](https://docs.python.org/3/library/sys.html) & [os](https://docs.python.org/3/library/os.html)

- style guide: [pep8](https://peps.python.org/pep-0008/)