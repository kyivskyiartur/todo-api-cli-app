# Todo API CLI App

A simple Python CLI application for creating and managing tasks using REST API requests.

## Features

- Create tasks through CLI
- Input validation
- Validate task title
- Validate completion status
- Send POST requests to REST API
- Save tasks locally to JSON file
- Load previously saved tasks
- Display task summaries

## Technologies Used

- Python
- requests
- JSON
- Git
- GitHub

## Project Structure

```text
todo-api-cli-app/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

Clone repository:

```bash
git clone https://github.com/kyivskyiartur/todo-api-cli-app.git
```

Go to project folder:

```bash
cd todo-api-cli-app
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Project

```bash
python main.py
```

## Example Workflow

```text
How many tasks you want to create? 2

Task 1 title: Learn Python
Completion status for task 1: true

Task 2 title: Learn APIs
Completion status for task 2: false
```

## Future Improvements

- Delete tasks
- Update tasks
- Batch requests
- OpenAI API integration
- Menu system
- Better task formatting
