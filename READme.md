# Expense and Budget Tracker

## Description

A web application for managing financial transactions using Flask and SQLAlchemy. The system allows users to view, edit, and delete transactions. The application uses SQLite for database storage.

## Features

- View a list of transactions

- View sum by category and month

- Edit transaction details

- Delete transactions with confirmation prompts

- Responsive and user-friendly interface

## Installation

### Prerequisites

- Python 3.9 or later

- Flask

- SQLAlchemy

### Steps to Install

1\. **Clone the repository:**

```bash
git clone https://github.com/lubasinkal/expense-and-budget.git    
```

2\. **Navigate into the project directory:**

```bash
cd backend
```

3\. **Create a virtual environment:**

```bash
python -m venv venv
```

4\. **Activate the virtual environment:**

   - On Windows:

```bash
venv\Scripts\activate
```

   - On macOS/Linux:

```bash
source venv/bin/activate
```

5\. **Install the required packages:**

```bash
pip install -r requirements.txt
```

6\. **Set up the database:**

   Initialize the database and create the required tables:

```bash
flask db upgrade
```

7\. **Run the application:**

```bash
flask run
```

## Usage

1\. **Access the Application**

   Open your browser and navigate to `http://127.0.0.1:5000/` to access the application.

2\. **View Transactions**

   The main page displays a nav bar and options to submit data i.e. .xlsx or .csv

3\. **Edit Transactions**

Click the "View Transactions" link then "Edit" button next to a transaction to update its details.

4\. **Delete Transactions**

Click the "Delete" button next to a transaction. A confirmation dialog will appear before deletion.

## Configuration

Configure your database connection in `config.py`:

```python
class Config:
SQLALCHEMY_DATABASE_URI = 'sqlite:///yourdatabase.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## Contributing

If you would like to contribute to this project, please follow these steps:

1\. Fork the repository.

2\. Create a new branch (`git checkout -b feature-branch`).

3\. Make your changes and commit them (`git commit -am 'Add new feature'`).

4\. Push to the branch (`git push origin feature-branch`).

5\. Create a new Pull Request.

```
if you have any suggestions on what i can improve on let me know
```

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) for the web framework

- [SQLAlchemy](https://www.sqlalchemy.org/) for ORM

- [SQLite](https://www.sqlite.org/) for the database

```

Feel free to customize any sections as needed based on your specific project requirements and details!
