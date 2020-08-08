# Review for CRUD Project

Congratulations on finishing the first project of your course! :clap::sparkles:

I hope you will the following reviews as motivation to futher develop your skill in Python Programming :snake::computer:

## Acknowledgement

In this section, I would like to say few words that I'm particularly impressed with. You have shown to gain proefficiency in the Python programming language, and these point show how you have learned so much.

### 1. **Importing Packages**

It seems you have done well in installing and importing the necessary pacakges for this assignment. Well done!

### 2. **Database Connection**

Looks Good :thumbsup: You seem to have a great understanding on usin SQL alchemy for connecting with SQL databases. Note that there are various database engine out there other than SQLite. If you wish to see how you can connect with different engines with SQL Alchemy, check out this [site](https://docs.sqlalchemy.org/en/13/core/engines.html).


### 3. **Creating Tables**

Good job in creating your own tables with SQL Alchemy! Based on the following lines of code, it should't be a problem for you to create any kinds of tables using SQL Alchemy.

```
students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('firstname', String), 
   Column('lastname', String), 
   Column('age', Integer), 
   Column('height', Integer)
)
meta.create_all(engine)
```

### 4. **Breaking program down into Functions**

One of the most important part of programming is breaking down cluttered lines of code into smaller parts. Breaking it down into functions allows for an easier process of debugging in the future. You have done well in just doing that :smile: I'd recommend you check out [this article](https://able.bio/rhett/python-functions-and-best-practices--78aclaa) for best practices on Python functions.

### 5. **Comprehensiveness in using Conditionals**

Understanding how to use conditonals is a fundamental part of programming. In this project, you have uses conditionals extensively and shows how to use it efficiently. Well done!

### 6. **Understanding of SQL Alchemy for CRUD Operations**

The CRUD project involves the basics of manipualting data through SQL realted opeartions. Using Pythong and the SQL Alchemy library, you have shown an understanding how to use them in order to interact with the database. I encourage you to checkout the [official documentaion](https://docs.sqlalchemy.org/en/13/orm/tutorial.html) for futher understanding of SQL Alchemy.

## Suggested Improvements

### 1. **Following the PEP8 Guide for Writing Beautiful Python Code**

I suggest you to check our the guideliens of PEP8. It shows some suggestion on how you can make your code more readable. This is important since great applications used by many people are mostly the result of not one, but many developers.

References:
- [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/)

### 2. **Optional: Combining Functions into a Class**

This one is optional unless you wish to futher extend this program or include it in a bigger project. Classes allow you organize your functions and data around a certain thing in a logical way. 

References:
- [Classes - Python Docs](https://docs.python.org/3/tutorial/classes.html)
- [Classes and Objects](https://www.learnpython.org/en/Classes_and_Objects)
- [Idiomatic Python: functions versus classes](https://devblogs.microsoft.com/python/idiomatic-python-functions-versus-classes/)
