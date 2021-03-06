# Flask_Guest_Book

This is a simple web application that takes the details of a guest attending an event or an organisation. This web app was built using `Flask` with `Python3` programming language and styled using `Bootstrap v3.3.7`

## Usage

Clone this repo into your local storage
`git clone https://github.com/Alienz11/Flask_Guest_Book.git`

A virtual evironment can be created if prefered. Run the following commands on your terminal

- [x] **Creating Virtual environment** :hammer_and_wrench:

  - Download Python3 on your system

    On your terminal/working directory run the following command

  - Install virtualenv to create a virtual environment

    ```
    user % pip3 install virtualenv
    ```

  - Create a virtual environment

    ```
    user % virtualenv < prefered environment name(i.e venv) >
    ```

  - Activate virtual environment

    ```
    user % source venv/bin/activate
    (venv) user %
    ```

- [x] **Creating Flask Web Framework** :hammer_and_wrench:

  - Installing Flask and SqlAlchemy (Database)

    ```
    (venv) user % pip3 install flask flask-sqlalchemy
    ```

- [x] **Creating Database** :hammer_and_wrench:

  - For personal mordifications, The file [models.py](src/models.py) is used to input the table and columns while creating the database. While [**init**.py](src/__init__.py) is used to create the app that initiates the database. The database can be named to any prefered name'
    `app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///<example.db>'`

  - Creating database, on terminal run the following

    ```
    (venv) user % python3
    >>> from src import db, create_app
    >>> from src.models import Comment
    >>> db.create_all(app=create_app())
    /Users/user/Library/Python/3.8/lib/python/site-packages/flask_sqlalchemy/__init__.py:872: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
    warnings.warn(FSADeprecationWarning(

    >>> exit()
    (venv) user %
    ```

- [x] **Starting The Flask App** :arrow_forward: :gear:

  - On the base repository (i.e The parent reposotory for `src/`), run the following.

    ```
    (venv) user % export FLASK_ENV=development    //This is to make the flaskapp run on debug mode
    (venv) user % export FLASK_APP=src         //The flaskapp=src because it holds all the files and would be used as a pakage.
    (venv) user % flask run                        //This starts the app
    * Serving Flask app 'src' (lazy loading)
    * Environment: development
    * Debug mode: on
    /Users/user/Library/Python/3.8/lib/python/site-packages/flask_sqlalchemy/__init__.py:872: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
    warnings.warn(FSADeprecationWarning(
    * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 123-456-789
    ```

  - click on the link `http://127.0.0.1:5000` and have fun :rocket::rocket::rocket:

- [x] **Live Deployment** :rocket::rocket:

  - The following files are needed for Flask live deployment build on either Netlify or in this project's case Heroku
    - [.flaskenv](.flaskenv)
    - [wsgi.py](wsgi.py)
    - [requirements.txt](requirements.txt)
    - [Procfile](Procfile)

Happy Coding :smile::smile::rocket:

## Demo

To see deployed app click [Guess_book_app](https://fl-guest-book.herokuapp.com/)
To log into Admin page, username and password is `Alienz11`

## References

- [pretty printed](https://www.youtube.com/c/PrettyPrintedTutorials)
- [Free Code Camp's Flask Tutorials](https://www.youtube.com/c/Freecodecamp)
