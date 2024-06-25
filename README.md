# ContentSphere Blog

ContentSphere Blog is a dynamic blogging platform built with Django, designed to provide an intuitive and engaging experience for both blog administrators and readers. It features a sleek admin interface powered by Jazzmin, comprehensive user authentication, and a rich set of models to support posts, categories, comments, and likes.

## Features

- **Dynamic Post Management**: Create, edit, and delete blog posts with ease.
- **Category System**: Organize posts into multiple categories for better navigation.
- **User Authentication**: Custom user model with email authentication.
- **Interactive Comments and Likes**: Engage your audience with interactive comments and likes on posts.
- **Customizable About and Contact Pages**: Easily update your about and contact information through the admin interface.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**

   ```sh
   git clone https://github.com/yourusername/contentsphere-blog.git
   cd contentsphere-blog
   ```

2. **Set up a virtual environment**

   ```sh
   python -m venv venv
   ```
   Activate the virtual environment:
   * On Windows:
    ```sh
    .\venv\Scripts\activate
    ```
   * On Unix or MacOS:
   ```sh
   source venv/bin/activate
   ```
3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up the database**
   Run the following command to create the necessary database tables:
   ```sh
   python manage.py migrate
   ```
5. **Create an admin user**
   To access the Django admin interface, you need to create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to set up your username, email, and password.
6. **Run the development server**
   ```sh
   python manage.py runserver
   ```
   The project will be available at http://127.0.0.1:8000/.

**Accessing the Admin Interface**
  Navigate to http://127.0.0.1:8000/admin/ and log in using the superuser credentials you created earlier to access the Django admin interface.

**Built With**
  Django - The web framework used
  Jazzmin - For the admin interface
