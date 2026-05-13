"""NAVTTC Advance Python — Master Reference

This single file is a compact, hands-on reference covering core and advanced
Python concepts, plus sample mini-projects and important practice questions.
"""

# ------------------------------
# 1) Basics: Variables & Types
# ------------------------------

name = "Navttc"
age = 26
pi = 3.14159
is_active = True
nothing = None

print("Basics:", name, age, pi, is_active, nothing)

# ------------------------------
# 2) Numbers & Math
# ------------------------------

import math

x = 10
print("Math:", x + 5, x - 3, x * 2, x / 4, x ** 2, x // 3, x % 4)
print("sqrt, ceil, floor:", math.sqrt(81), math.ceil(2.1), math.floor(2.9))

# ------------------------------
# 3) Strings
# ------------------------------

text = "Python is powerful"
print("Strings:", text.upper(), text.lower(), text.title())
print("Slicing:", text[0:6], text[-8:])
print("f-string:", f"{name} course level {age}")

# ------------------------------
# 4) Lists
# ------------------------------

nums = [1, 2, 3, 4, 5]
nums.append(6)
nums.extend([7, 8])
nums.remove(2)
print("List:", nums, nums[0], nums[-1])

# List comprehension
squares = [n * n for n in nums]
print("Squares:", squares)

# ------------------------------
# 5) Tuples
# ------------------------------

point = (10, 20)
print("Tuple:", point[0], point[1])

# ------------------------------
# 6) Sets
# ------------------------------

set_a = {1, 2, 3, 3}
set_b = {3, 4, 5}
print("Sets:", set_a, set_a | set_b, set_a & set_b, set_a - set_b)

# ------------------------------
# 7) Dictionaries
# ------------------------------

student = {"name": "Ayesha", "age": 20, "grade": "A"}
student["city"] = "Lahore"
print("Dict:", student)

# ------------------------------
# 8) Control Flow
# ------------------------------

score = 87
if score >= 90:
    level = "Excellent"
elif score >= 75:
    level = "Good"
else:
    level = "Needs Improvement"
print("If/elif/else:", level)

# Loops
for i in range(3):
    print("For loop:", i)

count = 0
while count < 3:
    print("While loop:", count)
    count += 1

# ------------------------------
# 9) Functions
# ------------------------------


def greet(user: str) -> str:
    return f"Hello, {user}!"


print(greet("NAVTTC"))

# Default args and *args/**kwargs

def add(a, b=0):
    return a + b


def sum_all(*args):
    return sum(args)


def describe(**kwargs):
    return ", ".join(f"{k}={v}" for k, v in kwargs.items())


print("Functions:", add(5, 3), sum_all(1, 2, 3, 4), describe(lang="Python", level="Advance"))

# ------------------------------
# 10) Lambda & Higher-Order
# ------------------------------

nums2 = [1, 2, 3, 4, 5]
print("Lambda map:", list(map(lambda n: n * 2, nums2)))
print("Lambda filter:", list(filter(lambda n: n % 2 == 0, nums2)))

# ------------------------------
# 11) Files (Text)
# ------------------------------

sample_path = "sample.txt"
with open(sample_path, "w", encoding="utf-8") as f:
    f.write("Hello NAVTTC\nPython File Handling")

with open(sample_path, "r", encoding="utf-8") as f:
    content = f.read()
print("File content:\n", content)

# ------------------------------
# 12) Exceptions
# ------------------------------

try:
    result = 10 / 0
except ZeroDivisionError as exc:
    print("Exception:", exc)
finally:
    print("Finally always runs")

# ------------------------------
# 13) OOP: Classes
# ------------------------------


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        return f"{self.name} is {self.age} years old"


p = Person("Ali", 22)
print("OOP:", p.intro())


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def intro(self):
        return f"{self.name} ({self.roll_no}) is {self.age} years old"


s = Student("Sana", 21, "NAV-101")
print("Inheritance:", s.intro())

# ------------------------------
# 14) Dataclasses
# ------------------------------

from dataclasses import dataclass


@dataclass
class Course:
    title: str
    duration: int


c = Course("Advance Python", 12)
print("Dataclass:", c)

# ------------------------------
# 15) Generators
# ------------------------------


def countdown(n):
    while n > 0:
        yield n
        n -= 1


print("Generator:", list(countdown(5)))

# ------------------------------
# 16) Decorators
# ------------------------------


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@logger
def multiply(a, b):
    return a * b


print("Decorator:", multiply(3, 4))

# ------------------------------
# 17) Itertools
# ------------------------------

import itertools

print("Itertools:", list(itertools.islice(itertools.count(10, 2), 5)))

# ------------------------------
# 18) Comprehensions
# ------------------------------

matrix = [[1, 2], [3, 4]]
flat = [item for row in matrix for item in row]
print("Comprehensions:", flat)

# ------------------------------
# 19) JSON
# ------------------------------

import json

data = {"course": "Python", "level": "Advance", "students": 30}
json_str = json.dumps(data)
parsed = json.loads(json_str)
print("JSON:", json_str, parsed)

# ------------------------------
# 20) Modules & Packages
# ------------------------------

# Example only: create reusable modules in separate .py files.
print("Modules: Use 'import module_name' to reuse code")

# ------------------------------
# 21) Type Hints
# ------------------------------

from typing import List


def average(values: List[int]) -> float:
    return sum(values) / len(values)


print("Type hints:", average([10, 20, 30]))

# ------------------------------
# 22) Context Managers
# ------------------------------

from contextlib import contextmanager


@contextmanager
def managed_resource():
    print("Acquire resource")
    yield "RESOURCE"
    print("Release resource")


with managed_resource() as r:
    print("Using", r)

# ------------------------------
# 23) Collections
# ------------------------------

from collections import Counter, defaultdict, deque

counts = Counter("python")
print("Counter:", counts)

bag = defaultdict(list)
bag["fruits"].append("apple")
print("Defaultdict:", dict(bag))

queue = deque([1, 2, 3])
queue.append(4)
queue.popleft()
print("Deque:", queue)

# ------------------------------
# 24) Dates & Times
# ------------------------------

from datetime import datetime, timedelta

now = datetime.now()
print("Datetime:", now.strftime("%Y-%m-%d %H:%M"))
print("Tomorrow:", (now + timedelta(days=1)).date())

# ------------------------------
# 25) Regular Expressions
# ------------------------------

import re

pattern = r"\bPython\b"
print("Regex:", re.findall(pattern, "I love Python and Python"))

# ------------------------------
# 26) Command Line Args
# ------------------------------

# Use: python master_python_reference.py arg1 arg2
import sys
print("CLI args:", sys.argv)

# ------------------------------
# 27) Testing (unittest)
# ------------------------------

import unittest


class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)


# Note: Run with `python -m unittest master_python_reference.py`

# ------------------------------
# 28) Asyncio Basics
# ------------------------------

import asyncio


async def async_task():
    await asyncio.sleep(0.1)
    return "Async done"


async def run_async():
    result = await async_task()
    print("Asyncio:", result)


asyncio.run(run_async())

# ------------------------------
# 29) Web Requests (optional)
# ------------------------------

# Requires `requests` library: pip install requests
# import requests
# response = requests.get("https://api.github.com")
# print("Requests status:", response.status_code)

# ------------------------------
# 30) Simple Project Structure Guidance
# ------------------------------

print("Project tip: Use src/, tests/, requirements.txt, and README.md")

# =====================================================================
# IMPORTANT QUESTIONS + READY-MADE SAMPLE PROJECTS (All-in-one)
# =====================================================================

print("\n--- IMPORTANT QUESTIONS + SAMPLE PROJECTS ---\n")

# 1) Calculate sum and average of a list of numbers
numbers = [10, 20, 30, 40, 50]
sum_numbers = sum(numbers)
avg_numbers = sum_numbers / len(numbers)
print("Q1 Sum:", sum_numbers, "Average:", avg_numbers)

# 2) Consuming an API (Streamlit frontend app)
# Save this block as api_frontend_app.py and run: streamlit run api_frontend_app.py
api_frontend_app = """\
import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title=\"REST API Consumer\", layout=\"wide\")
st.title(\"RESTful API Consumer Frontend\")
st.write(\"Consumes JSONPlaceholder API and displays data.\")

BASE_URL = \"https://jsonplaceholder.typicode.com\"
endpoint = st.selectbox(\"Select endpoint:\", [\"posts\", \"users\", \"comments\", \"albums\", \"todos\"])

if st.button(\"Fetch Data\"):
    url = f\"{BASE_URL}/{endpoint}\"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
"""

# 3) Visualizations (bar chart, pie chart)
import pandas as pd
import matplotlib.pyplot as plt

products = pd.DataFrame(
    {"Category": ["Electronics", "Clothing", "Food"], "Count": [25, 35, 40]}
)
products.plot(x="Category", y="Count", kind="bar", legend=False, title="Product Distribution")
plt.tight_layout()
plt.show()

plt.figure()
plt.pie(products["Count"], labels=products["Category"], autopct="%1.1f%%")
plt.title("Product Distribution")
plt.show()

# 4) Image classification (skeleton with Keras)
# Requires: tensorflow
image_classification_template = """\
import tensorflow as tf
from tensorflow.keras import layers, models

model = models.Sequential([
    layers.Rescaling(1./255, input_shape=(128, 128, 3)),
    layers.Conv2D(16, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(3, activation='softmax')  # cats, dogs, birds
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
"""

# 5) Sort dictionary by values
scores = {"Alice": 85, "Bob": 92, "Eve": 78, "David": 88}
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1]))
print("Q5 Sorted scores:", sorted_scores)

# 6) Read file, process, write output
# Example processing: uppercase all lines
input_path = "input.txt"
output_path = "output.txt"
with open(input_path, "w", encoding="utf-8") as f:
    f.write("hello\nnavttc\npython")

with open(input_path, "r", encoding="utf-8") as f:
    processed = [line.strip().upper() for line in f]

with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(processed))

# 7) Creating RESTful API with Django REST Framework (project template)
django_rest_api_template = """\
# Install: pip install django djangorestframework
# Create project: django-admin startproject student_api_project
# Create app: python manage.py startapp api
# Add 'rest_framework' and 'api' to INSTALLED_APPS
# Define Student model, serializer, and ViewSet
# Use DefaultRouter to register /api/students/
"""

# 8) Inheritance with Animal -> Dog/Cat
class Animal:
    def speak(self):
        return "..."


class Dog(Animal):
    def speak(self):
        return "Woof Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


dog = Dog()
cat = Cat()
print("Q8:", f"Dog says: {dog.speak()}, Cat says: {cat.speak()}")

# 9) Customer purchase prediction (classification skeleton)
ml_classification_template = """\
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# data = pd.read_csv('customers.csv')
# X = data.drop('purchase', axis=1)
# y = data['purchase']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)
# model = LogisticRegression()
# model.fit(X_train, y_train)
# print(classification_report(y_test, model.predict(X_test)))
"""

# 10) Flask-Login authentication (template)
flask_login_template = """\
from flask import Flask, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'secret'

login_manager = LoginManager(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

users = {'admin': {'password': 'admin123'}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            login_user(User(username))
            return redirect(url_for('protected'))
    return 'Login Page'

@app.route('/protected')
@login_required
def protected():
    return 'Protected Page'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out'
"""

# 11) Shape base class with Circle and Rectangle
class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle(5)
rectangle = Rectangle(4, 6)
print("Q11:", f"Circle Area: {circle.area():.2f}, Rectangle Area: {rectangle.area()}")

# 12) Read file and display contents with error handling
try:
    with open("input.txt", "r", encoding="utf-8") as f:
        print("Q12 Contents:\n", f.read())
except FileNotFoundError:
    print("Q12: input.txt not found")

# 13) Sentiment trends from reviews (simple keyword approach)
reviews = [
    ("Great product", "positive"),
    ("Bad quality", "negative"),
    ("Excellent service", "positive"),
]
trend = Counter(sentiment for _, sentiment in reviews)
print("Q13 Sentiment trend:", trend)

# 15) Common keys between dictionaries
dict1 = {"A": 1, "B": 2, "C": 3}
dict2 = {"B": 4, "C": 5, "D": 6}
common_keys = set(dict1) & set(dict2)
print("Q15 Common keys:", common_keys)
