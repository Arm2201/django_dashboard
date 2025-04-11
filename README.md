# Django Custom Admin Dashboard

This is a custom-built admin dashboard created using **Django**. The dashboard includes user management, authorization controls, and a reporting interface. It's designed with a clean UI for internal use and showcases different user roles like Member, Staff, and Admin.

## 🔧 Features

- Custom login and registration forms
- Sidebar navigation with links to:
  - Dashboard Overview
  - Users list
  - Authorization panel (role management)
  - Reports page (user statistics)
  - Logout
- User list with real-time account data
- Role assignment via dropdown (Member, Staff, Admin)
- Reports with total users, active staff, and admins
- Stylish responsive interface with CSS customization

Run the following code in the terminal:
- python -m venv venv
- pip install django
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

Enjoy!

