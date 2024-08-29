<div align="center">
  <img src="logo.png" alt="Social Insecurity" width="538" height="96" />
</div>

## About the project
Social Insecurity is a social media web application lacking many key security features. Your goal is to identify what features are missing, and then proceed to implement them.

There are several comments in the code from the “previous developers”, who did not have the time to focus on security while developing the application. These comments may point you in a possible direction on how to improve the code, but of course you are free to choose your own path and implementation.

## Getting started

### Prerequisites

Social Insecurity requires Python 3.9 or higher to run. If you do not have Python installed, you can download it from the [official website](https://www.python.org/downloads/).

This project uses [Poetry](https://python-poetry.org/). It is a tool that simplifies the process of managing dependencies and virtual environments for Python projects. To install Poetry, follow the instructions in the [official documentation](https://python-poetry.org/docs/#installation).

> [!IMPORTANT]
> Poetry is a multi-platform tool, but occasionally it can be difficult to install on some operating systems. If you are having trouble, then try one of the alternative installation instructions for your operating system. If all else fails, the file `requirements.txt` can be used to install the required packages using pip.

### Installation

Create a copy of this repository by clicking the `Use this template` button at the top of this page. A new repository will be created on your GitHub account with the same directory structure and files as this repository.

> [!TIP]
> If you are unfamiliar with the process of creating a repository from a template, you can follow the [official instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template).

Clone the repository you created to your local machine, open a terminal in the root directory of the project, and run the command:

```shell
poetry install
```

A folder named `.venv` will be created in the root directory of the project. Poetry then proceeds to create a virtual environment and install the application’s dependencies, listed in the file `pyproject.toml`, into this folder.

> [!TIP]
> Modern IDEs, such as Visual Studio Code, PyCharm, Spyder, etc., should automatically detect the virtual environment created by Poetry and use it for the project. If not, you can manually select the virtual environment by following the instructions usually found on your IDE’s support pages.

### Important directories and files

Social Insecurity follows a standard Flask project structure. The most important directories and files are:

- `instance/`, a directory containing the `sqlite3.db` database file and user uploaded files. It is created when the application is started for the first time.
- `social_insecurity/`, a Python package containing the application files and code.
  - `social_insecurity/templates/`, a directory containing Jinja2 templates used to render HTML pages.
  - `social_insecurity/__init__.py`, a file where the application instance is created and configured.
  - `social_insecurity/config.py`, a file containing configuration parameters used to configure the application.
  - `social_insecurity/database.py`, a file where the database connection is created and configured.
  - `social_insecurity/forms.py`, a file containing form definitions used to create HTML forms.
  - `social_insecurity/routes.py`, a file where routes are defined and the main application logic is implemented.
  - `social_insecurity/schema.sql`, a file containing the SQL schema for the application database.
- `tests/`, a directory containing test modules.
- `.flaskenv`, a file containing application specific environment variables. This file is read by Flask when the application is started.
- `pyproject.toml`, a file containing information about the application and its dependencies.
- `social_insecurity.py`, a file containing the application‘s entry point. This file can be used to start the application.

## Usage

### Starting the application

To start the application, open a terminal in the root directory of the project, and run the command:

```shell
poetry run flask --debug run
```

> [!TIP]
> The `--debug` flag starts the application in debug mode. This mode enables the debugger, reloader, and other nice-to-have development features.

An alternative way to start the application is by executing the `social_insecurity.py` file using Python:

```shell
poetry run python social_insecurity.py
```

Access the application by entering `http://localhost:5000/` in the address bar of a web browser while the application is running.

> [!NOTE]
> Prepending `poetry run` to any command ensures that the command is run inside the virtual environment created by Poetry, and not in the global Python environment. As an example, the command `poetry run python -c "print('Hello World')"` prints `Hello World` to the terminal using the Python interpreter installed inside the project‘s virtual environment.

To stop the application, press <kbd>Ctrl</kbd>+<kbd>C</kbd> in the terminal where the application is running.

To reset the application back to its initial state, use:

```shell
poetry run flask reset
```

This deletes the `instance/` directory which contains the database file and user uploaded files.

### Adding, removing and updating dependencies

To add a dependency to the project, use the command:

```shell
poetry add <package-name>
```

> [!TIP]
> The command `poetry add -G dev <package-name>` adds a development dependency to the project. Development dependencies are dependencies which are not needed to run the application, they are only used during development and testing.

To remove a dependency, use:

```shell
poetry remove <package-name>
```

To update all dependencies to the newest version allowed by the version constraints specified in the `pyproject.toml` file:

```shell
poetry update
```

To only update specific dependencies, you can list them as arguments to the `update` command:

```shell
poetry update <package-name>
```

## Development

### Linting and formatting files

To ensure a consistent code style, all Python files have been linted and formatted using [Ruff](https://docs.astral.sh/ruff/), and Jinja2 templates have been linted and formatted using [djLint](https://www.djlint.com/). It is recommended that you lint and format files before you commit then to your repository.

#### Python

To lint all Python files in the project directory and fix any fixable errors, use the command:

```shell
poetry run ruff check --fix
```

> [!TIP]
> By default, Ruff is configured with a limited number of linting rules. If you wish to add additional linting rules, you can find instructions on how to do this in the [official documentation](https://docs.astral.sh/ruff/linter/).

To format the all Python files, use:

```shell
poetry run ruff format
```

#### Jinja2

To lint all Jinja2 templates in the `templates` directory:

```shell
poetry run djlint social_insecurity/templates/ --lint
```

To format all templates:

```shell
poetry run djlint social_insecurity/templates/ --reformat
```

### Inspecting the database

During development, you might like to inspect the SQLite database generated and used by the application. A good, multi-platform program for this task is [DB Browser for SQLite](https://sqlitebrowser.org). To install it, follow the [official installation instruction](https://sqlitebrowser.org/dl/).

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
