# World of Kid's Drawings
Welcome to the World of Kid's Drawings project! This is a Django-based web application that allows parents, visitors, and staff to engage with a platform centered around children's drawings. Parents can register, add their kids, and associate drawings with them. Visitors can explore drawings and user profiles, while staff members have additional privileges to manage kids and drawings.

## Features
### Home Page and User Roles:
- ``` Not authenticated users ```: Can explore drawings only.
  
![Screenshot of Home page](https://github.com/1van101/Final-Django-Project-Exam/blob/main/staticfiles/images/home-screen.jpg)

- ``` Parent ```: Can register, log in, add kids, and associate drawings with their kids.
- ``` Visitor ```: Can explore drawings, view user profiles, and profiles of their linked kids.
- ``` Staff ```: Can manage kids for other parents and add drawings for any kid.

### Authentication and Authorization:

- Secure user registration:
- Login system:
### Kid and Drawing Management:

- Parents can add and manage their kids.
- Parents can upload drawings and link them to their kids.
- Staff can manage kids for all parents and add drawings for any kid.

### Installation
- Clone this repository to your local machine using git clone ``` [https://github.com/1van101/Final-Django-Project-Exam.git] ```
- Navigate to the project directory: ``` cd Final-Django-Project-Exam ```
- Create a virtual environment: ``` python -m venv venv ```
- Activate the virtual environment:
- ``` On Windows: venv\Scripts\activate ```
- ``` On macOS and Linux: source venv/bin/activate ```
- Install the project dependencies: ``` pip install -r requirements.txt ```
- Set up the database:
  - Run migrations: ``` python manage.py migrate ```
  - Create a superuser (for full access): ``` python manage.py createsuperuser ```
  - Start the development server:``` python manage.py runserver ```
  - Access the application in your web browser at ``` http://127.0.0.1:8000/ ```
### Usage
- Register as a parent or visitor using the provided registration forms.
- Parents can log in and add their kids.
- Parents can upload drawings and associate them with their kids.
- Visitors can explore drawings and view user profiles.
- Staff can log in and manage kids for all parents, as well as add drawings.

## License
This project is licensed under the MIT License.

