# Learning Log

A simple Django web app that lets users track topics they're learning about and write journal entries as they go.

## 📖 About

Learning Log is a personal learning journal built with Django. 
The home page describes the site and invites visitors to register or log in. 
Once logged in, a user can create topics they're interested in, add journal entries under each topic, and read or edit existing entries.

This is a beginner Django project built while learning the framework 
— it focuses on core concepts like models, views, templates, user authentication, and forms.

## ✨ Features

- User registration and login/logout
- Create new learning topics
- Add journal entries under each topic
- Read and edit existing entries
- Per-user data (each user only sees their own topics and entries)
- Django admin panel for managing data

## 🛠️ Tech Stack

- **Backend:** Django, Python
- **Database:** SQLite
- **Frontend:** Django templates, Bootstrap
- **Tools:** Git, GitHub, VS Code

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/bmunyiri/learning-log.git
   cd learning-log


2. **Create and activate a virtual environment**
   python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

3. **Install dependencies**
   pip install -r requirements.txt

4. **Apply migrations**
   python manage.py migrate

5. **Create a superuser (optional — for admin access)**
   python manage.py createsuperuser

6. **Run the development server**
   python manage.py runserver

🧭 How to Use
Visit the home page and register a new account (or log in if you already have one).

From the topics page, click "Add a new topic" to create a topic you want to learn about.

Click on a topic to view its entries, then add a new entry describing what you learned.

Edit existing entries anytime from the topic page.

🗂️ Project Structure
text
learning-log/
├── manage.py
├── requirements.txt
├── .gitignore
├── learning_log/          # project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── learning_logs/         # main app
    ├── models.py          # Topic, Entry
    ├── views.py
    ├── urls.py
    ├── forms.py
    └── templates/
Adjust the app names above if yours differ (e.g., learning_logs vs another name).

📚 What I Learned
Setting up a Django project and app

Defining models and running migrations

Using Django's built-in authentication system

Building views with @login_required

Creating forms with ModelForm

Working with templates and template inheritance

Using Git and GitHub for version control

🤝 Feedback
This is a learning project — feedback, suggestions, and tips are very welcome! Feel free to open an issue or reach out.

👤 Author
Bernard Munyiri

GitHub: @bmunyiri



