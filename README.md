# Access Key Manager
  An access key manager platform to help school administrators generate keys to activate thier school accounts.
## 🎯 Project Objective
Micro-Focus Inc., a software company, has built a school management platform that is multitenant. This project aims to create an access key manager for schools to purchase access keys to activate their school account.

## 🛠 Features
--- User Features ---
  - 🔑 Signup & Login: Users can register and log in using email and password. Includes account verification and password recovery.

  - Access Key Management: Users can generate keys and track the status and expiration dates of the key.

--- Admin Features ---
  - ⚙️ Manage Keys: Admins can revoke keys created by other users on the platform.
  - Separate Dashboards for Admin and Non-Admin Users

## 📋 Deliverables
- Source Code: Available  here on [GitHub](https://github.com/Mustapha7018/Video-Platform) with a well-written README.
- ER Diagram: Included in the repository.
- Deployed Link: [veedeo.pythonanywhere.com](https://veedeo.pythonanywhere.com/)

## ER Diagram Description
  - User

    - id: Primary Key
    - email: Unique Email
    - password: Hashed Password
    - is_staff: Boolean (indicates if the user is an admin)

  - Access Key
    - id: Primary Key
    - user : Foreing Key to User
    - key: string
    - status : string
    - date_procured : DateTime
    - expiry_date : DateTime

  
## 🚀 Getting Started
### Prerequisites
- Python 3.x
- Django 5.x
- Other dependencies listed in `requirements.txt`

### Installation
1. Clone the repository
```
git clone https://github.com/Mustapha7018/Video-Platform.git
```
2. Navigate to the project directory
```
cd Video-Platform
```
3. Install dependencies
```
pip install -r requirements.txt
```

### Running the Application
1. Apply Migrations:
```
python manage.py migrate
```
2. Create a superuser for admin access:
```
python manage.py createsuperuser
```
3. Run the development server:
```
python manage.py runserver
```
4. Access the application at `http://127.0.0.1:8000`.

## 🧪 Unit Tests
### Running Unit Tests
To ensure the integrity of the application, unit tests have been written to cover various functionalities. To run the unit tests, use the following command:
```
python manage.py test
```

## 🛠️ Django Workflow
### GitHub Actions
The project uses GitHub Actions for Continuous Integration (CI). The workflow is defined in the `.github/workflows/access_key_tests.yml` file. This setup ensures that tests are automatically run on each push and pull request to the repository.

### Setting Up Github Actions
1. Ensure the `.github/workflows/access_key_tests.yml` file is present in the repository.
2. The workflow will automatically trigger on pushes and pull requests to the repository, running the specified tests and checks.
3. This integration helps maintain code quality and streamline the development process.


## 📊 ER DIAGRAM
![image]()