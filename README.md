# Suman Website

This repository contains the source code for the Suman Website. This project is a simple Flask-based web application designed to serve static company information pages and handle customer inquiries through a contact form.

---

## Table of Contents

* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Running the Application](#running-the-application)
* [Features](#features)
* [Contact Form Submissions](#contact-form-submissions)
* [Frontend Files](#frontend-files)
* [Future Enhancements](#future-enhancements)
* [License](#license)
* [Acknowledgements](#acknowledgements)

---

## Getting Started

To get a local copy of this project up and running on your machine, follow these simple steps.

### Prerequisites

Ensure you have the following installed:

* **Python 3.8+**: You can download it from [python.org](https://www.python.org/).
* **pip**: Python's package installer, usually included with Python installations.

### Installation

1.  **Clone the repository (if applicable) or set up your project directory:**
    If you're starting from scratch, create your project directory (e.g., `suman_website`) and place your `app.py`, `static/`, and `templates/` files inside it as described in the [Project Structure](#project-structure) section.

    If you've cloned the repository, navigate into the project's root directory:
    ```bash
    cd suman_website # Example: cd ~/Downloads/sumanwebsite
    ```

2.  **Create a Python virtual environment (highly recommended):** This isolates your project dependencies from other Python projects.
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **On Windows:**
        ```bash
        venv\Scripts\activate
        ```

4.  **Install Flask:** With your virtual environment activated, install Flask using pip:
    ```bash
    pip install Flask
    ```

### Running the Application

1.  **Ensure your virtual environment is activated.**
2.  **Run the Flask application:**
    ```bash
    flask run
    ```
    Alternatively, you can run:
    ```bash
    python app.py
    ```

3.  **Access the application:** Open your web browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

The console where you ran `flask run` will display messages, including contact form submissions.

---


## Features

* **Static Page Serving**: Renders pre-built HTML pages for different sections of the website.
* **Contact Form Handling**: Processes form submissions from the "Contact Us" page, logging the data to the console and providing user feedback via flash messages.
* **Dynamic News Section**: Demonstrates how to pass dynamic data (news articles) from the Flask backend to an HTML template.
* **Static File Management**: Correctly serves CSS and image assets.
* **Responsive Design**: (Inherited from frontend) The frontend is designed to be responsive across various devices.

---

## Contact Form Submissions

The `contact.html` page includes a form that, upon submission, sends a `POST` request to the Flask backend. The `app.py` currently handles this by:

* Retrieving the submitted **name**, **email**, and **message**.
* Printing these details to the console where the Flask application is running.
* Displaying a success message to the user using Flask's `flash` system.

**Note:** For a production application, you would typically integrate this with a database for storage (e.g., using Flask-SQLAlchemy) or an email service to send notifications.

---

## Frontend Files

The project utilizes the following HTML and CSS files for the frontend:

* `templates/index.html`: The main landing page.
* `templates/introduction.html`: Details about the company.
* `templates/products.html`: Information about products.
* `templates/solutions.html`: Details on company solutions.
* `templates/customer.html`: Customer information.
* `templates/contact.html`: Contact form for inquiries.
* `templates/news.html`: Displays dynamic news articles fetched from the backend.
* `static/css/style.css`: Contains the global styling for the website.
* `static/images/`: Contains various image assets used throughout the site.

---

## Future Enhancements

* **Database Integration**: Replace the in-memory `news_articles` list and potentially contact form logging with a proper database (e.g., SQLite, PostgreSQL) using Flask-SQLAlchemy or Flask-SQLModel.
* **Email Sending**: Implement actual email sending for contact form submissions (e.g., using Flask-Mail or a direct SMTP library).
* **Form Validation**: Add server-side validation for contact form fields to ensure data integrity and security.
* **Admin Panel**: Create a simple admin interface to manage news articles, contact inquiries, etc.
* **User Authentication**: If needed, add user login/registration functionality.
* **Error Pages**: Implement custom 404 (Not Found) and 500 (Internal Server Error) pages.

---

## License

This project is open source and available under the **MIT License**. (You can change this to your preferred license).

---

## Acknowledgements

* Thanks to the Flask community for providing an excellent web framework.
* (Add any other acknowledgements here, e.g., for design resources, tutorials, etc.)
