 vikki-prod
A Django project built with Python.

Setup Instructions

1.Clone the repository
   bash
   git clone https://github.com/your-username/vikki-prod.git
   cd vikki-prod
   
2.Create a virtual environment
python -m venv .venv

3.Activate the virtual environment

On Linux / macOS:
source .venv/bin/activate

On Windows (PowerShell):
.venv\Scripts\Activate.ps1

4.Install dependencies
pip install -r requirements.txt

5.Create database table
python manage.py makemigrations

6.Apply database migrations
python manage.py migrate


7.Run the development server
python manage.py runserver
