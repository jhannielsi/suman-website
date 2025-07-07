Getting Started
To get a local copy up and running, follow these simple steps.
Prerequisites
Python 3.8+
pip (Python package installer)
Installation
Clone the repository (if applicable) or set up your project directory:
If you're starting from scratch, create the your_project_name directory and place app.py, static/, and templates/ inside it as described in the Project Structure.
Navigate into your project directory:
cd your_project_name


Create a Python virtual environment (recommended):
python -m venv venv


Activate the virtual environment:
On macOS/Linux:
source venv/bin/activate


On Windows:
venv\Scripts\activate


Install Flask:
pip install Flask


Running the Application
Ensure your virtual environment is activated.
Run the Flask application:
flask run

Alternatively, you can run:
python app.py


Access the application:
Open your web browser and navigate to: http://127.0.0.1:5000
The console where you ran flask run will display messages, including contact form submissions.
