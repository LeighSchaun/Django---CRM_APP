# Django---CRM_APP
This Django application is a simple CRM (Customer Relationship Management) app that allows users to keep track of their customer records. Users can add, view, edit, and delete customer records. Users must first register and log in before they can access the application's features.

Installation
Clone the repository to your local machine using git clone https://github.com/your_username/your_project.git
Install the required dependencies by running pip install -r requirements.txt
Create a .env file in the root directory of the project and add your secret key in the following format: SECRET_KEY=your_secret_key_here
Run migrations using python manage.py migrate
Start the server using python manage.py runserver
Usage
Registration and Login
Users must first register for an account before they can access the application's features. Click on the 'Register' link on the navigation bar and fill out the form. After registering, users can log in with their credentials.

Viewing Customer Records
After logging in, users will be directed to the home page, which displays all the customer records added by the user. Clicking on a customer record will redirect the user to a page that displays the details of the customer.

Adding Customer Records
To add a customer record, click on the 'Add Record' button on the home page, fill out the form, and submit it. The customer record will be added to the user's list of customer records.

Editing Customer Records
To edit a customer record, click on the 'Edit' button on the customer record details page. This will redirect the user to a page where they can edit the customer record's details.

Deleting Customer Records
To delete a customer record, click on the 'Delete' button on the customer record details page. The customer record will be permanently deleted from the user's list of customer records.

Logging Out
To log out of the application, click on the 'Log Out' link on the navigation bar.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT
