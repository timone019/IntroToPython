# Recipe App Command Line Version

## Objective
Build a command line version of a Recipe app, which acts as a precursor to its web app counterpart in Achievement 2.

## Context
Develop a command line version of a Recipe app, serving as a foundational step towards its web application counterpart in Achievement 2.

Creating a website with the Django web framework is predominantly done in Python, leveraging its object-oriented capabilities. Understanding Python's core concepts and syntax is crucial, especially when adapting to updates in Django. This project emphasizes Python fundamentals, data structures, and object-oriented programming, providing a solid base for interacting with databases using Python. These skills will be invaluable when transitioning to Django for web development. Additionally, the project aims to instill standard programming practices, ensuring your code is clean, readable, and robust.

## User Goals
Users should be able to effortlessly create and modify recipes, including details such as ingredients, cooking time, and an automatically calculated difficulty level. They should also be able to search for recipes based on ingredients.

## Key Features
- Manage recipes on a locally hosted MySQL database.
- Search for recipes containing specific ingredients.
- Automatically assign a difficulty rating to each recipe.
- Display detailed information about each recipe, including ingredients, cooking time, and difficulty level.

## Technical Requirements
- Handle common exceptions and errors gracefully, providing user-friendly error messages.
- Connect to a locally hosted MySQL database.
- Offer an intuitive interface with simple input forms and clear instructions, assuming users may not be technically proficient.
- Ensure compatibility with Python 3.6+.
- Maintain well-formatted code adhering to standardized guidelines.
- Include concise, helpful comments to illustrate the program's flow.

## Nice to Have
- Robust input handling to manage unexpected or nonsensical user inputs, simulating "monkey testing" manually to test the application's limits.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/recipe-app-cli.git
   cd recipe-app-cli
2. **Set up a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the application:**
   ```sh
   python main.py

## Usage
1. **Activate the virtual environment:**
   ```sh
   source venv/bin/activate
2. **Run the application:**
   ```sh 
   python main.py  


# Python Environment Setup Guide

## 1. Install Python

### macOS
1. **Install Homebrew** (if not already installed):
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
### Install Python
    ```sh
    brew install python@3.12
Windows
1. Download Python Installer from the official Python website.
2. Run the Installer:
- Make sure to check the box "Add Python to PATH."
- Select "Customize installation" and then "Install for all users."
## 2. Install virtualenvwrapper
### macOS and Linux
1. Install virtualenvwrapper using pip (may need to use pip3 instead of pip):
   ```sh
    python3 -m pip install --user virtualenvwrapper
2. Update .zshrc or .bashrc:
   ```sh
   # Set the directory for virtual environments
    export WORKON_HOME=$HOME/.virtualenvs

    # Set the Python interpreter for virtualenvwrapper
    export VIRTUALENVWRAPPER_PYTHON=$(which python3)

    # Source the virtualenvwrapper script
    source $(which virtualenvwrapper.sh)
3. Apply Changes:
    ```sh
   source ~/.zshrc  # or ~/.bashrc if using bash
### Windows 
1. Install virtualenvwrapper-win using pip: 
   ```sh
   python -m pip install virtualenvwrapper-win
## 3. Create and Manage Virtual Environments
### Create a New Virtual Environment
    ```sh
    mkvirtualenv cf-python-base
### Activate a Virtual Environment
    ```sh
    workon cf-python-base
### Deactivate a Virtual Environment
    ```sh
    deactivate
### Create a New Virtual Environment of the Existing Virtual Environment
    ```sh
    mkvirtualenv cf-python-copy
## 4. Install Packages & Export Requirements
### Install iPython
    ```sh
    pip install ipython
### Export Installed Packages to requirements.txt
    ```sh
    pip freeze > requirements.txt
### Install Packages from requirements.txt in a New Environment
1. Create and activate the new environment.
2. Run: 
    ```sh
    pip install -r requirements.txt
## 5. Using iPython Shell
### Start iPython 
1. Activate the virtual environment
2. Run:
    ```sh
    ipython
## 6. Troubleshooting
### Common Errors
- Error: externally-managed-environment
    - Ensure you are in a virtual environment when installing packages.
    - Use pip from within the activated virtual environment.
- Error: ModuleNotFoundError
    - Verify that the virtualenvwrapper package is installed and sourced correctly.
- Error: ValueError: too many values to unpack (expected 3)
    - Ensure the text file is in plain text format and correctly formatted.
## 7. Additional Notes
- Always activate the appropriate virtual environment before installing or managing packages.
- Use pip freeze to track package dependencies and ensure consistent environments.
- You may need to adjust or update any specifics relevant to your setup or use case!




