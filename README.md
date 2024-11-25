
# 📝 Mini Blog Project

Welcome to the **Mini Blog**! This project is a permission-based blogging platform built using Django for both the frontend and backend. It includes a robust admin panel, allowing different types of users to manage blog posts based on their roles.

## 📖 Features

### User Roles
1. **Author**  
   - Has full permissions to:
     - Add new blog posts.
     - Edit existing blog posts.
     - Update blog posts.
     - Delete blog posts.

2. **Person**  
   - Has limited permissions to:
     - Create new blog posts.
     - Edit their own blog posts.
     - Update their own blog posts.

### Django Admin Panel
- The platform is managed via the Django Admin panel.
- Superusers (Admins) have full access to manage users and permissions.

### Frontend & Backend
- **Frontend:** Built using Django templates for seamless user interaction.
- **Backend:** Django REST API for database communication and CRUD operations.

---

## 🛠️ Technologies Used
- **Python**: Backend logic
- **Django**: Web framework
- **Django REST Framework**: API connection
- **SQLite** (default): Database

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine:

### Prerequisites
1. Install Python (3.8 or higher) from [python.org](https://www.python.org/downloads/).
2. Install pip, the Python package installer.
3. Ensure Django is installed:  
   ```bash
   pip install django
   ```

---

### Setup Instructions

1. **Clone the Repository**  
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/mini-blog.git
   ```
   Navigate into the project folder:
   ```bash
   cd mini-blog
   ```

2. **Install Dependencies**  
   Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**  
   Apply the database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a Superuser**  
   To access the Django Admin panel, create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up a username, email, and password.

5. **Run the Development Server**  
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```
   Access the application at:  
   - User-facing site: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
   - Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📂 Project Structure

```
mini-blog/
├── blog/                  # Main app for blog functionality
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   ├── views.py           # View logic
│   └── models.py          # Data models
├── mini_blog/             # Project configuration
│   ├── settings.py        # Project settings
│   └── urls.py            # URL routing
├── db.sqlite3             # SQLite database (auto-created after migrations)
├── manage.py              # Django's CLI utility
└── requirements.txt       # Python dependencies
```

---

## 🧑‍💻 How to Use

### For Superusers
- Log in to the admin panel at `/admin/` to manage users, roles, and posts.
- Superusers can access and modify all aspects of the application.

### For Authors
- Authors can:
  - Add, edit, update, and delete blog posts.
  - Manage their own content directly from the site.

### For Persons
- Persons can:
  - Create new blog posts.
  - Edit and update their own blog posts.

---

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-branch
   ```
5. Create a pull request.

---

## 📧 Contact

For queries or suggestions, feel free to contact:
- **Your Name**
- **Email**: your-email@example.com
- **GitHub**: [your-username](https://github.com/your-username)

---

### 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy coding! 🎉
