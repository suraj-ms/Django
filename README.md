# Django Project Setup

This guide outlines the steps to set up a Django project in a virtual environment.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python (3.6 or higher)
- pip (Python package installer)
- virtualenv (optional, can also use `venv`)

## Steps to Create a Django Project

### 1. Install virtualenv (if not using venv)

If you haven't installed `virtualenv`, you can do so by running:

```bash
pip install virtualenv
```
### 2. Create a Virtual Environment

Navigate to the directory where you want to create your Django project, then create a virtual environment:

```bash
cd /path/to/your/project/directory
virtualenv env
```

This creates a folder named env containing the virtual environment.

### 3. Activate the Virtual Environment

Activate the virtual environment with the following command:

<ul>
<li>
    <b>On Windows:</b>

    cd /path/to/your/project/directory

    virtualenv env
    
</li>
<br/>
<li>
    <b>On macOS/Linux:</b>
    
    cd /path/to/your/project/directory

    source env/bin/activate
</li>
</ul>

You should see (venv) at the beginning of your terminal prompt, indicating that the virtual environment is active.

### 4. Install Django

With the virtual environment activated, install Django using pip:

``` bash
pip install django
```

### 5. Create a New Django Project

Now, you can create a new Django project. Replace myproject with your desired project name:

``` bash
django-admin startproject <project-name>
```

### 6. Run the Development Server

Navigate into your project directory:

```bash
cd myproject
```

Run the development server:


```bash
python manage.py runserver
```

You should see output indicating that the server is running. Open your web browser and go to http://127.0.0.1:8000/ to view your new Django project.

### 7. Deactivating the Virtual Environment

When you're done working on your project, you can deactivate the virtual environment by simply running:

```bash
deactivate
```


## Django db

Pyhton has built it data table access that table we need to migrate the django

```bash
python manage.py migrate
```

Now you can create your model in model class and after adding all data model now migrate the database

```bash
python manage.py makemigrations
```
now re migrate with <b> python manage.py migrate</b> command 

## Django administator 

now to create a user in django admin run following command add fill the data

```bash
python manage.py createsuperuser
```

To access the admin panel use <b>/admin</b> url in browser

Now add you model in admin.py then you can see your model in adminstation panel

Then access the database like
<pre>
room = Room.objects.get(id = pk)
                   .all()
                   .filter
</pre>