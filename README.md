# flask_app

## Notes
1. On url, at "http://localhost:5000/static/my_name.txt" displays the content of the file "my_name.txt"
2. Go to "getbootstrap.com", and there click 'Docs' to go to 'Getting started'
3. Copy the code available at 'starter_template' in "https://getbootstrap.com/docs/5.0/getting-started/  introduction/", and paste it at the 'index.html' of our project.
4. After writing the 'TodoDatabase' class, open the python interpreter. Execute the following commands one after another:
   >>> from app import db
   >>> db.create_all()
Now, see that a file 'honey_todo.db' file is created. This is how we have created our database.
Type 'exit()' at the interpreter to exit.
5. Pick and drop 'honey_todo.db' file at 'https://inloop.github.io/sqlite-viewer/'. And the see the command.
6. see the "https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application" to work around the SQLAlchemy database.
7. After adding in SQLAlchemy database, pick and drop 'honey_todo.db' file at 'https://inloop.github.io/sqlite-viewer/'. And the see the added content.
8. Add "Jinja2 Snippet Kit" extension in Vscode. With this, we can use Jinja templating. 
9. Template Inheritance :- Suppose there are search bars on 100 html pages, and I need to remove them. I would remove them manually. If I had used Inheritance template, I could have removed it from all the pages.
10. Read "https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#"