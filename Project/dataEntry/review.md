# Review for Django Data Entry Project

Wow second project done! Congratulations! :fire::thumbsup:

You are on your way to becoming Djangonaut :rocket: I hope this review could you to persue futher moonshot projects using Django :moon:

## Acknowledgement

In this section, I would like to say few words that I'm particularly impressed with. You have shown to gain comprehension in using the Django framework, and these point show how you have learned so much.

### 1. **Starting a Django Project**

Good job with this one :punch: thr first step in working on a Djago project is starting one. Django provides a number of files to help you jumpstart bulding your backend. You even used a virtual environment, which is a great way to make sure that certain dependencies are isolated so they don't clash with other dependencies :smiley:

### 2. **Configuration in settings.py**

One of the earliest steps of working with a Django project is making sure that the database is configured in the `DATABASES` variable, and if there are any thid party app to be included in the `INSTALLED_APPS` variable. You seem to be doing just that here, Greate Job :star:

In addition, if you wish to connec to a database in a remote server, you could set `DATABASES` to something like this

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'POSTGRES_DB_NAME',
        'USER': 'POSTGRES_USER',
        'PASSWORD': 'POSTGRES_DB_PASSWORD',
        'HOST': 'SERVER_IP_ADDRESS'
    }
}
```

Note that when a Django project is used in production, make sure to set `DEBUG` to `False`.

### 3. **Dedicated Directoy for Tempaltes**

Well done! You've created a separate directory for storing the templates. Doing this will help you to organize other teplates as you work on any Django project.

### 4. **Starting an Application**

Django also provide starting files for creating applications using the command `startapp`. Job well done on doing just that! If you wish to learn more about the `startapp` command, I hight recommend the [documentation](https://docs.djangoproject.com/en/3.1/ref/django-admin/#startapp) page.

### 5. **Utilizing Views, URLS, and Models to Manipulate Data**

Understanding views, urls, and models is essential in order to query or do any other kind of manipualtions of data. Looking at the code implementations, you have a comprehensive understanding on how to connect these 3 elements together to retrieve or create data. Great :clap::sparkler:

### 6. **Impementation of Forms**

Good job! Forms are important for receiving inputs from end-users. Those inputs will then will be inserted to the database via models. There are more to forms than meets the eye, so I would definitely suggest you to check out the [documentation](https://docs.djangoproject.com/en/3.1/topics/forms/) on forms.

### 6. **Displaying Data on Templates using Jinja**

Awesome! This is part is quite tricky. One of the most important elements of Django is the templates. They are basically text document or a Python string marked-up that allows you to display data on the frontend. To do that, to do that Django utilizes Jinja, which is a templating language for Python. There are more to be learend on Django templates. For that reason, I highly recommencd [this artile](https://medium.com/@MicroPyramid/basics-of-django-templates-e2916f791492) for further understanding.

## Suggested Improvements

### 1. **Django's Coding Style**

Since Django is built on top of Python, it only make sense that certain coding styles are suggested. This is important when your Django project gets more complex and you need more than one developer to work on it. If that happens, then you need to follow certain guidlines to make your code more readable and matainable.

References:
- [Django Coding Style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)
- [Tips for Building High-Quality Django Apps at Scale](https://medium.com/@DoorDash/tips-for-building-high-quality-django-apps-at-scale-a5a25917b2b5)

### 2. **Using Environmental Variables**

This is important if you wish to put your Django project in production. Some information such as `SECRET_KEY` and database password are better to be stored seperate from your source code. It is best practice to store them as environmental variables.

References:
- [Django-environ’s](https://django-environ.readthedocs.io/en/latest/)
- [Django settings](https://docs.djangoproject.com/en/3.1/topics/settings/)

### 3. **Working with Images**

In case you wish to work image data, Django provide some built in functionality that would allow you to do that. I would suggest use [ImageKit](https://github.com/matthewwithanm/django-imagekit) to work with images.
