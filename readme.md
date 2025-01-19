# Bug Tracking System

![Bug Tracking System](/static/img/homepage.png)

A comprehensive Bug Tracking System designed to streamline issue management and improve collaboration among teams. This system ensures efficient bug reporting, assignment, and resolution while providing insightful dashboards and reporting tools.

---

## Live Demo

Check out the live application: [Bug Tracking System Live](https://chaitanya33.pythonanywhere.com/)


---

## This Repository also has [Dependency Checker](/checker.md).

## Key Features

### **User Authentication and Role Management**
- Admin, Developer, and Tester roles with specific permissions.
- User registration and login with hashed passwords.

### **Bug Logging and Tracking**
- Create, update, and delete bug reports.
- Assign bugs to specific developers.
- Set bug priorities (low, medium, high) and statuses (open, in-progress, resolved, closed).

### **Dashboard**
- Separate dashboards for Admin, Developers, and Testers.
- Admin dashboard for monitoring all bugs.
- Developer dashboard for bugs assigned to them.

### **Email Notifications**
- Automatic email alerts for status updates or assignments.

### **Bug Search and Filtering**
- Search by bug title, status, or priority.
- Filter bugs by developer or creation date.

### **Reports**
- Generate reports on bug trends (e.g., resolved vs. open bugs) using `matplotlib`.

---

## Tech Stack and Libraries

### **Deployment**
![PythonAnywhere](https://img.shields.io/badge/pythonanywhere-%232F9FD7.svg?style=for-the-badge&logo=pythonanywhere&logoColor=151515)

### **Backend**
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


### **Frontend**
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

### **Database**
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### **Email Notifications**
- `django.core.mail.backends.console.EmailBackend` for testing email functionality.

### **Visualization**
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

---

## Setup Guidelines

Refer to [setup.md](./Setup.md) for step-by-step instructions to set up the project locally.

---

## Contribution

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.