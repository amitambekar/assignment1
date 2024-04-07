# Readme

## Prerequisites
Before you begin, ensure you have the following installed:
- Python (version 3.10 recommended)
- pip package manager

## Installation
1. Clone or download the repository from [GitHub link](https://github.com/your-repo).
2. Navigate to the project directory using the command line.

## Setup
1. Create a virtual environment to isolate the project's dependencies:

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:
      ```bash
      source venv/bin/activate
      ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application
1. Ensure you are in the project directory and your virtual environment is activated.
2. Run the Flask application:

    ```bash
    flask run
    ```

3. By default, the application will be accessible at `http://127.0.0.1:5000` in your web browser.

## Usage
1. create model endpoint:
  - http://127.0.0.1:5000/create_model with **POST**
2. to get all project metadata:
  - http://127.0.0.1:5000/get_project_metadata with **GET**
