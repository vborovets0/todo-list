# ToDo List

"ToDo List" is a Django-based project, that is visualised into a site. On this site you can create tasks, mark them as
done (or make undo to completion), see deadlines, when it was created, what you need to do and its tags.

You can create, update and delete all objects - both tasks and tags.

## Installation

1. Copy this repository, by using your terminal:

```git
git clone https://github.com/vborovets0/todo-list.git
```

2. Change directory to main project folder. Use this command:

```git
cd todo-list
```

3. Install venv, and activate it by using following commands:

```git
python3 -m venv myvenv
```

to activate on Windows:

```git
myvenv\Scripts\activate
```

to activate on Unix or Linux:

```git
source myvenv/bin/activate
```

4. Install dependencies (requirements):

```git
pip install -r requirements.txt
```

5. Run migrations to initialize database. Use this command:

```git
python manage.py migrate
```

6. Run the server of app

```git
python manage.py runserver
```

## About .env

In main folder you'll find a file .env_sample. In this file an example of SECRET_KEY is stored, required for the
project.

You need to rename a file ".env_sample" to ".env" and write here you secret key.

## Demo

![Website Interface](demo.png)