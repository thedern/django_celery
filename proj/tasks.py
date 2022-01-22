# import Celery Class
from .celery import app
from time import sleep

# run all functions with 'delay'
# example:  reverse.delay('darren')

@app.task
def add(x, y):
    return x + y


@app.task
def mult(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task
def reverse(text):
    return text[::-1]