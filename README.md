# Student Management System

A full-stack web application built with Python and Django for managing student records, course enrollments, and administrative workflows.

## Tech Stack
* **Backend:** Python, Django
* **Database:** SQLite / PostgreSQL
* **Frontend:** HTML5, CSS3, Django Templates

## Project Architecture
* `students/`: Main application containing domain logic, models, forms, and views.
* `student_mgmt/`: Root configuration module containing project settings and primary URL routing.

## Setup & Installation

1. Clone the repository:
   git clone https://github.com/Nishanth4063/student_mgmt_system.git
   cd student_mgmt_system

2. Set up a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run migrations and start the server:
   python manage.py migrate
   python manage.py runserver