Sticky Notes

A lightweight Django web application for creating, editing, and managing sticky notes.
Built to provide a simple and intuitive way to jot down quick notes.

Features:

- Create new notes with a title and body

- View a list of all saved notes

- Edit or delete existing notes

- Clean, minimal interface with custom styling

Getting Started:

- Prerequisites:

  - Python 3.10+

  - Django 5+
 
Installation:
1.Clone the repository:
  git clone <your-repo-url>
  cd sticky_notes

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows

3. Install the dependencies:
   pip install -r requirements.txt

4. Apply database migrations:
   python manage.py migrate

5. Start the development server:
   python manage.py runserver

6. Open the app in your browser:
   http://127.0.0.1:8000/

Customization:
- Edit styles in notes/static/notes/styles.css
- Template modification in notes/templates/notes/



