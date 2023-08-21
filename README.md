# World of Kid's Drawings
Welcome to the World of Kid's Drawings project! This is a Django-based web application that allows parents, visitors, and staff to engage with a platform centered around children's drawings. Parents can register, add their kids, and associate drawings with them. Visitors can explore drawings and user profiles, while staff members have additional privileges to manage kids and drawings.

## Features
### Home Page and User Roles:
- ``` Not authenticated users ```: Can explore drawings only.
 ![Alt Text](https://github.com/1van101/Final-Django-Project-Exam/blob/main/staticfiles/images/home-screen.jpg)
- ``` Parent ```: Can register, log in, add kids, and associate drawings with their kids.
- ``` Visitor ```: Can explore drawings, view user profiles, and profiles of their linked kids.
- ``` Staff ```: Can manage kids for other parents and add drawings for any kid.
![Alt Text](https://github.com/1van101/Final-Django-Project-Exam/blob/main/staticfiles/images/home-screen-staff.jpg)

### Authentication and Authorization:

- Secure user registration:
![Alt Text](https://github.com/1van101/Final-Django-Project-Exam/blob/main/staticfiles/images/register-screen.jpg)
- Login system:
![Alt Text](https://github.com/1van101/Final-Django-Project-Exam/blob/main/staticfiles/images/login-screen.jpg)
### Kid and Drawing Management:

- Parents details page.
![Alt Text](https://github.com/1van101/Final-Django-Project-Exam/blob/main/staticfiles/images/profile-details.png)

- Filter kid's drawings by name in parent profile details.
![Alt Text](https://github.com/1van101/Final-Django-Project-Exam/blob/main/staticfiles/images/profile-details-filter.png)

- Parents edit page.
![Alt Text](https://github.com/1van101/Final-Django-Project-Exam/blob/main/staticfiles/images/profile-edit.png)

- Parents can add and manage their kids.
![Alt Text](https://github.com/1van101/Final-Django-Project-Exam/blob/main/staticfiles/images/add-kid-screen.jpg)

- Parents can upload drawings and link them to their kids.
![Alt Text](https://github.com/1van101/Final-Django-Project-Exam/blob/main/staticfiles/images/add-drawing-screen.jpg)

- Staff can manage kids for all parents and add drawings for any kid.



- Drawings likes and comment section:
![Alt Text](https://github.com/1van101/Final-Django-Project-Exam/blob/main/staticfiles/images/drawing-likes-comments.png)

- Who liked the drawing container: 
![Alt Text](https://github.com/1van101/Final-Django-Project-Exam/blob/main/staticfiles/images/likes-container.jpg)

- Edit drawing page: 
![Alt Text](https://github.com/1van101/Final-Django-Project-Exam/blob/main/staticfiles/images/edit-drawing-screen.jpg)

- Details drawing page: 
![Alt Text](https://github.com/1van101/Final-Django-Project-Exam/blob/main/staticfiles/images/drawing-details.png)


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

