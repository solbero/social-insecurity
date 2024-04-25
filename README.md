<img style="display:block;margin:auto" src="logo.png" alt="Social Insecurity" width="538" height="96" />

## About the project
Social Insecurity is a social media web application lacking many key security features. Your goal is to identify as many of these as possible, and then proceed to patch them.

There are several comments in the code from the “previous developers” who did not have the time to focus on security while developing the application. These comments may point you in a possible direction on how to improve the code, but of course you are free to choose your own path and implementation.

## Getting started

### Prerequisites

- Python 3.9 or greater
- [Poetry](https://python-poetry.org/)

> [!TIP]
> This project uses Poetry as dependency manager. Poetry is a tool for finding, downloading, and installing Python packages. It also handles the creation of a virtual environment to isolate the dependencies of an application.

There are several different ways you can [install](https://python-poetry.org/docs/#installation) Poetry, the recommended way is to use [pipx](https://pipx.pypa.io/). To install pipx, you should follow the [official installation instructions](https://pipx.pypa.io/stable/installation/#installing-pipx) for your operating system.

After you have installed pipx, install Poetry using pipx:
```shell
pipx install poetry
```

Check that Poetry is working:
```shell
poetry about
```

> [!CAUTION]
> If the above command gives an error, try log out of your operating system and then log back in.

> [!IMPORTANT]
> Both Poetry and pipx are multi-platform tools, but sometimes they can be difficult to install due to different system or hardware configurations. If you are having trouble, then try one of the alternative installation instructions for your operating system. If all else fails, the file `requirements.txt` can be used to [install the required packages](https://pip.pypa.io/en/stable/user_guide/#requirements-files) using pip.

### Installation

Create a new repository using this repository as a template. You can follow the [official instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template) if you are unsure on how to do this.

Create a local clone of your new repository. Again, if you are unsure on how to do this you can follow the [official instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository).

> [!TIP]
> This project is configured to use Visual Studio Code as the IDE, but of course you can use any IDE you want. The configuration for Visual Studio Code includes extension recommendations and some default settings for this project. You can install the recommended extensions by opening the command palette (<kbd>Ctrl</kbd>+<kbd>shift</kbd>+<kbd>P</kbd>) and entering the command `Extensions: Show Recommended Extensions`.

Within the root folder of this application, there is a `pyproject.toml` file, which lists all the Python dependencies necessary to run the application. To install all the required dependencies listed in this file in a virtual environment using Poetry, open a terminal in the project’s root folder and run the command:

```shell
poetry install
```

> [!TIP]
> Modern IDEs, such as Visual Studio Code, PyCharm, Spyder, etc., should automatically detect the virtual environment created by Poetry and use it for this project. If not, you can manually select the virtual environment by following the instructions usually found on your IDE’s support pages.

### Structure

```shell
social-insecurity
├── social_insecurity
│   ├── static
│   │   └── css
│   │       └── general.css
│   ├── templates
│   │   ├── alert.html.j2
│   │   ├── base.html.jinja
│   │   ├── comments.html.j2
│   │   ├── friends.html.j2
│   │   ├── index.html.j2
│   │   ├── profile.html.j2
│   │   └── stream.html.j2
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── forms.py
│   ├── routes.py
│   └── schema.sql
├── instance
│   ├── uploads
│   └── sqlite3.db
├── tests
│   └── test_routes.py
├── .flaskenv
├── .gitignore
├── LICENSE.md
├── poetry.toml
├── pyproject.toml
├── README.md
├── requirements.txt
└── socialinsecurity.py
```

The most important files and directories:
- `social_insecurity/`: This directory is the root of the application, this is from where the pages are served.
  - `social_insecurity/static/`: Directory containing static content. Files such as CSS and JavaScript can be stored here and accessed from anywhere in the application.
  - `social_insecurity/templates/`: Directory containing all the HTML files in a template format. This allows the application to display content dynamically, by integrating logical operators and variables into HTML. These files are populated once the user requests one of the sites.
  - `social_insecurity/__init__.py`: Initializes the application.
  - `social_insecurity/config.py`: Contains the configuration for the application.
  - `social_insecurity/database.py`: Contains the database connection and functions for interacting with the database.
  - `social_insecurity/forms.py`: Defines the forms that the users will use to input information.
  - `social_insecurity/routes.py`: Implements the routing between different pages, handles form input and database calls.
  - `social_insecurity/schema.sql`: Defines the database tables, and their relations.
- `instance/`: Directory containing the instance files, which is not committed to version control. This is where the database file and user uploads are stored.
- `tests/`: Directory containing simple integration tests for the application.
- `.flaskenv`: Contains the environment variables for the application.
- `.gitignore`: Contains the files and directories that should not be committed to version control.
- `pyproject.toml`: Contains the application dependencies and their configuration.
- `socialinsecurity.py`: The entry point for the application.

## Usage
### Starting the application
Use the following command to start the Flask application in debug mode:

```shell
poetry run flask --debug run
```

You should now be able to access the application through your web browser by entering [127.0.0.1:5000](http://127.0.0.1:5000) in the address bar.

> [!NOTE]
>  By prepending `poetry run` to any command you will run it inside the virtual environment created by Poetry. As an example, if you wish to run the Python interpreter installed in the project’s virtual environment you can use the command `poetry run python`.

### Adding a dependency
To install a new dependency:

```shell
poetry add <package-name>
```

### Removing a dependency
To remove a dependency:

```shell
poetry remove <package-name>
```

### Updating dependencies
To update all dependencies:

```shell
poetry update
```

### Linting project files

[Ruff](https://docs.astral.sh/ruff/) is the linter used to lint all Python files in this project. By default, Ruff is configured with a limited number of linting rules. If you wish to add additional linting rules, you can find instructions on how to do this in the [official documentation](https://docs.astral.sh/ruff/linter/).

Lint all Python files:
```shell
poetry run ruff check
```

> [!TIP]
> Ruff is a drop-in replacement for [flake8](https://flake8.pycqa.org/en/latest/), [isort](https://pycqa.github.io/isort/) and many other linters. This means that any rules from these projects most likely are available for Ruff. As an example, there exists a rule to enable [flake8-bandit](https://github.com/tylerwince/flake8-bandit) as a static code analyser in Ruff.

[djLint](https://www.djlint.com/) is used to lint the Jinja2 templates in this project. If you wish to learn more about how to use djLint as a linter a look at the [official documentation](https://www.djlint.com/docs/linter/).

Lint all Jinja2 templates:
```shell
poetry run djlint social_insecurity/templates/ -e html.j2
```

### Formatting project files

Ruff is also used as the Python formatter for this project. You can find more information on how to use the ruff formatter in the [official documentation](https://docs.astral.sh/ruff/formatter/)

Format all Python files:
```shell
poetry run ruff format
```

> [!TIP]
> Ruff is a drop-in replacement for the [Black](https://black.readthedocs.io/) formatter.

djLint also includes a formatter for Jinja2 templates. Information on how to use djLint as a formatter can be found in the [official documentation](https://www.djlint.com/docs/formatter/).

Format all Jinja2 files:
```shell
djlint poetry run djlint social_insecurity/templates/ -e html.j2 --reformat
```

### Inspecting the database

During development, you might like to inspect the SQLite database generated and used by the application. A good multi-platform application for this is DB Browser for SQLite. To install the application follow the [official installation instruction](https://sqlitebrowser.org/dl/).

## Useful resources

### Tutorials
- [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [The Flask Quickstart guide](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
- [SQL Tutorial](https://www.w3schools.com/sql/)
- [Oh My Git!: An open source game about learning Git!](https://ohmygit.org/)

### Documentation
- [Flask documentation](https://flask.palletsprojects.com/)
- [Poetry documentation](https://python-poetry.org/)
- [Flask-WTF documentation](https://flask-wtf.readthedocs.io/)
- [SQLite3 documentation](https://docs.python.org/3/library/sqlite3.html)
- [Ruff documentation](https://docs.astral.sh/ruff/)
- [djLint documentation](https://www.djlint.com/)

## Questions
If you have any questions or problems, don't hesitate to contact me, and I will get back to you as soon as possible.
