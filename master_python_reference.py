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

st.set_page_config(page_title="REST API Consumer", layout="wide")
st.title("RESTful API Consumer Frontend")
st.write("Consumes JSONPlaceholder API and displays data.")

BASE_URL = "https://jsonplaceholder.typicode.com"
endpoint = st.selectbox("Select endpoint:", ["posts", "users", "comments", "albums", "todos"])

if st.button("Fetch Data"):
    url = f"{BASE_URL}/{endpoint}"
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

# =====================================================================
# ADVANCED PRACTICE (Exam-Style) SOLUTIONS (All-in-one)
# =====================================================================

print("\n--- ADVANCED PRACTICE (Exam-Style) ---\n")

# Q1: Advanced String Parser and Validator
attendance_records = [
    "EMP001 | Ali Khan | checkin=09:10 | checkout=17:45 | dept=IT",
    "EMP002|Sara|checkin=09:40|checkout=18:00|dept=HR",
    "EMP003 | Ahmed Raza | checkin=10:05 | checkout=16:50 | dept=Finance",
    "EMP001 | Ali Khan | checkin=09:15 | checkout=17:40 | dept=IT",
    "EMP004 | | checkin=09:00 | checkout=17:00 | dept=IT",
    "EMP005 | Hina | checkin=9x:20 | checkout=17:10 | dept=HR",
    "EMP006 | Zoya | checkin=08:55 | checkout= | dept=Finance",
    "Wrong Format Line",
]

id_pattern = re.compile(r"^EMP\d{3}$")
time_pattern = re.compile(r"^\d{2}:\d{2}$")

valid_attendance = []
invalid_attendance = []
seen_ids = set()


def clean_line(line):
    return " | ".join(part.strip() for part in line.strip().split("|"))


def is_valid_name(name):
    return bool(name) and all(ch.isalpha() or ch.isspace() for ch in name)


def is_valid_time(t):
    if not time_pattern.match(t):
        return False
    hh, mm = map(int, t.split(":"))
    return 0 <= hh <= 23 and 0 <= mm <= 59


for raw in attendance_records:
    line = clean_line(raw)
    if line.count("|") != 4:
        invalid_attendance.append((raw, "Wrong number of fields"))
        continue

    parts = [p.strip() for p in line.split("|")]
    emp_id, name, checkin_part, checkout_part, dept_part = parts

    if not id_pattern.match(emp_id):
        invalid_attendance.append((raw, "Invalid employee ID"))
        continue

    if emp_id in seen_ids:
        invalid_attendance.append((raw, "Duplicate employee ID"))
        continue

    if not is_valid_name(name):
        invalid_attendance.append((raw, "Invalid name"))
        continue

    if "checkin=" not in checkin_part or "checkout=" not in checkout_part or "dept=" not in dept_part:
        invalid_attendance.append((raw, "Wrong field format"))
        continue

    checkin = checkin_part.split("=", 1)[1].strip()
    checkout = checkout_part.split("=", 1)[1].strip()
    dept = dept_part.split("=", 1)[1].strip()

    if not checkin:
        invalid_attendance.append((raw, "Missing checkin"))
        continue
    if not checkout:
        invalid_attendance.append((raw, "Missing checkout"))
        continue
    if not is_valid_time(checkin) or not is_valid_time(checkout):
        invalid_attendance.append((raw, "Invalid time format"))
        continue

    seen_ids.add(emp_id)

    t_in = datetime.strptime(checkin, "%H:%M")
    t_out = datetime.strptime(checkout, "%H:%M")
    duration_minutes = int((t_out - t_in).total_seconds() / 60)

    valid_attendance.append(
        {
            "id": emp_id,
            "name": name,
            "checkin": checkin,
            "checkout": checkout,
            "dept": dept,
            "duration": duration_minutes,
        }
    )

print(f"{'ID':<8}{'Name':<15}{'Dept':<10}{'CheckIn':<8}{'CheckOut':<8}{'Duration':<10}")
print("-" * 59)
for r in valid_attendance:
    hours = r["duration"] // 60
    mins = r["duration"] % 60
    print(f"{r['id']:<8}{r['name']:<15}{r['dept']:<10}{r['checkin']:<8}{r['checkout']:<8}{hours:02}:{mins:02}")

print("\nInvalid Records:")
for raw, reason in invalid_attendance:
    print(f"{reason}: {raw}")

# Q2: Nested Data Structure Analyzer
quiz_data = {
    "BSCS": {
        "Semester1": [("Ali", [8, 7, 9]), ("Sara", [9, 10, 8]), ("Ahmed", [4, 5, 6])],
        "Semester2": [("Hina", [7, 8, 7]), ("Zoya", [10, 9, 10]), ("Bilal", [3, 4, 5])],
    },
    "BSSE": {
        "Semester1": [("Usman", [6, 7, 6]), ("Areeba", [10, 10, 9])],
        "Semester2": [("Danish", [5, 5, 6]), ("Maha", [9, 8, 9])],
    },
}


def status(avg):
    if avg >= 9:
        return "Excellent"
    if avg >= 7:
        return "Good"
    if avg >= 5:
        return "Average"
    return "Weak"


def flatten_students(data):
    flat = []
    for program, semesters in data.items():
        for semester, students in semesters.items():
            for name, scores in students:
                avg = sum(scores) / len(scores)
                flat.append(
                    {
                        "program": program,
                        "semester": semester,
                        "name": name,
                        "scores": scores,
                        "average": avg,
                    }
                )
    return flat


flat = flatten_students(quiz_data)

for s in flat:
    total = sum(s["scores"])
    print(s["program"], s["semester"], s["name"], total, f"{s['average']:.2f}", status(s["average"]))

# Topper of each program
program_toppers = {}
for s in flat:
    prog = s["program"]
    if prog not in program_toppers or s["average"] > program_toppers[prog]["average"]:
        program_toppers[prog] = s
print("Topper each program:", {k: v["name"] for k, v in program_toppers.items()})

# Weakest student overall
weakest = min(flat, key=lambda x: x["average"])
print("Weakest:", weakest["name"])

# Program averages (dict comprehension)
program_avg = {
    prog: sum(s["average"] for s in flat if s["program"] == prog)
    / len([s for s in flat if s["program"] == prog])
    for prog in quiz_data
}
print("Program averages:", program_avg)

# Unique scores (set comprehension)
unique_scores = {score for s in flat for score in s["scores"]}
print("Unique scores:", unique_scores)

# Sort by average desc, name asc
sorted_students = sorted(flat, key=lambda x: (-x["average"], x["name"]))
print("Sorted:", [s["name"] for s in sorted_students])

# Q3: File-Based Text Intelligence System
import string


def clean_word(word):
    return word.strip(string.punctuation).lower()


def is_palindrome(word):
    return word == word[::-1]


try:
    with open("article.txt", "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print("File missing.")
else:
    if not text.strip():
        print("File is empty.")
    else:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        cleaned = " ".join(lines)
        cleaned = cleaned.translate(str.maketrans("", "", string.punctuation))
        words = [w.lower() for w in cleaned.split() if w.strip()]

        total_chars = len(cleaned)
        total_words = len(words)
        unique_words = set(words)

        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1

        top5 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        longest = max(words, key=len)
        shortest = min(words, key=len)
        palindromes = [w for w in unique_words if is_palindrome(w) and len(w) > 1]
        once = [w for w, c in freq.items() if c == 1]

        report = [
            f"Total chars: {total_chars}",
            f"Total words: {total_words}",
            f"Unique words: {len(unique_words)}",
            f"Lines: {len(text.splitlines())}",
            f"Non-empty lines: {len(lines)}",
            f"Top 5 words: {top5}",
            f"Longest word: {longest}",
            f"Shortest word: {shortest}",
            f"Palindromes: {palindromes}",
            f"Words used once: {once}",
        ]

        with open("analysis_report.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(report))
finally:
    print("Text analysis complete.")

# Q4: Modular Library Management System (single-file version)
from pathlib import Path


class DuplicateBookError(Exception):
    pass


class DuplicateMemberError(Exception):
    pass


class BookNotFoundError(Exception):
    pass


class MemberNotFoundError(Exception):
    pass


class NoCopiesError(Exception):
    pass


class BookNotBorrowedError(Exception):
    pass


class Book:
    def __init__(self, book_id, title, author, total):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total = total
        self.available = total

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.available}/{self.total})"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed = []

    def __str__(self):
        return f"{self.member_id}: {self.name}, borrowed: {self.borrowed}"


class Library:
    def __init__(self, db_path="library_db.json"):
        self.books = {}
        self.members = {}
        self.db_path = Path(db_path)
        self.load()

    def add_book(self, book):
        if book.book_id in self.books:
            raise DuplicateBookError()
        self.books[book.book_id] = book

    def add_member(self, member):
        if member.member_id in self.members:
            raise DuplicateMemberError()
        self.members[member.member_id] = member

    def search_by_id(self, book_id):
        if book_id not in self.books:
            raise BookNotFoundError()
        return self.books[book_id]

    def search_by_title(self, keyword):
        return [b for b in self.books.values() if keyword.lower() in b.title.lower()]

    def issue_book(self, book_id, member_id):
        book = self.search_by_id(book_id)
        if member_id not in self.members:
            raise MemberNotFoundError()
        if book.available == 0:
            raise NoCopiesError()
        book.available -= 1
        self.members[member_id].borrowed.append(book_id)

    def return_book(self, book_id, member_id):
        if member_id not in self.members:
            raise MemberNotFoundError()
        if book_id not in self.members[member_id].borrowed:
            raise BookNotBorrowedError()
        self.members[member_id].borrowed.remove(book_id)
        self.books[book_id].available += 1

    def save(self):
        data = {
            "books": {k: vars(v) for k, v in self.books.items()},
            "members": {k: vars(v) for k, v in self.members.items()},
        }
        self.db_path.write_text(json.dumps(data, indent=2))

    def load(self):
        if self.db_path.exists():
            data = json.loads(self.db_path.read_text())
            for b in data.get("books", {}).values():
                book = Book(b["book_id"], b["title"], b["author"], b["total"])
                book.available = b["available"]
                self.books[book.book_id] = book
            for m in data.get("members", {}).values():
                member = Member(m["member_id"], m["name"])
                member.borrowed = m["borrowed"]
                self.members[member.member_id] = member


if __name__ == "__main__":
    lib = Library()
    while True:
        print("\n1.Add Book 2.Add Member 3.Issue 4.Return 5.Search 6.Available 7.Member 8.Save&Exit")
        choice = input("Choice: ")
        try:
            if choice == "1":
                lib.add_book(Book(input("ID:"), input("Title:"), input("Author:"), int(input("Total:"))))
            elif choice == "2":
                lib.add_member(Member(input("ID:"), input("Name:")))
            elif choice == "3":
                lib.issue_book(input("Book ID:"), input("Member ID:"))
            elif choice == "4":
                lib.return_book(input("Book ID:"), input("Member ID:"))
            elif choice == "5":
                print(lib.search_by_id(input("Book ID:")))
            elif choice == "6":
                for b in lib.books.values():
                    print(b)
            elif choice == "7":
                mid = input("Member ID:")
                print(lib.members[mid])
            elif choice == "8":
                lib.save()
                break
        except Exception as e:
            print("Error:", type(e).__name__)

# Q5: Recursive Folder-Like Data Processor
file_system = {
    "root": {
        "documents": {"resume.docx": 120, "report.pdf": 850, "notes.txt": 40},
        "images": {"profile.png": 300, "banner.jpg": 700},
        "projects": {
            "python": {"main.py": 25, "utils.py": 15, "README.md": 10},
            "web": {"index.html": 20, "style.css": 18},
        },
    }
}


def print_tree(node, indent=0):
    # base case: file (int size)
    if isinstance(node, int):
        return
    # recursive case: folder
    for name, content in node.items():
        if isinstance(content, dict):
            print("  " * indent + f"{name}/")
            print_tree(content, indent + 1)
        else:
            print("  " * indent + f"{name} - {content} KB")


def total_size(node):
    if isinstance(node, int):  # base case
        return node
    return sum(total_size(v) for v in node.values())  # recursive case


def find_largest(node, path=""):
    largest = ("", 0)
    for name, content in node.items():
        if isinstance(content, dict):
            cand = find_largest(content, path + name + "/")
            if cand[1] > largest[1]:
                largest = cand
        else:
            if content > largest[1]:
                largest = (path + name, content)
    return largest


def count_files_folders(node):
    files = 0
    folders = 0
    for content in node.values():
        if isinstance(content, dict):
            folders += 1
            f, fo = count_files_folders(content)
            files += f
            folders += fo
        else:
            files += 1
    return files, folders


def search_file(node, filename, path=""):
    if not filename:
        return None
    for name, content in node.items():
        if isinstance(content, dict):
            found = search_file(content, filename, path + name + "/")
            if found:
                return found
        else:
            if name == filename:
                return path + name
    return None


def report(*args):
    for item in args:
        print(item)


print_tree(file_system)
print("Total size:", total_size(file_system))
largest = find_largest(file_system["root"], "root/")
print("Largest:", largest)
files, folders = count_files_folders(file_system["root"])
print("Files:", files, "Folders:", folders)
top_sizes = {k: total_size(v) for k, v in file_system["root"].items()}
print("Top folder sizes:", top_sizes)
print("Search:", search_file(file_system, "report.pdf"))

# Q6: Mini Banking Transaction Engine
transactions = [
    "TXN001, ACC1001, deposit, 5000",
    "TXN002, ACC1001, withdraw, 1200",
    "TXN003, ACC1002, deposit, 7000",
    "TXN004, ACC1001, transfer, 1000, ACC1002",
    "TXN005, ACC1003, withdraw, 500",
    "TXN006, ACC1002, withdraw, -300",
    "TXN002, ACC1001, deposit, 2000",
    "BAD LINE HERE",
    "TXN007, ACC1002, transfer, 1500, ACC9999",
]

accounts = {"ACC1001": 10000, "ACC1002": 8000, "ACC1003": 300}


class InvalidTransactionError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


class DuplicateTransactionError(Exception):
    pass


class AccountNotFoundError(Exception):
    pass


class Account:
    def __init__(self, acc_id, balance):
        self.id = acc_id
        self.balance = balance
        self.history = []


class Transaction:
    def __init__(self, tid, acc, ttype, amt, receiver=None):
        self.tid = tid
        self.acc = acc
        self.ttype = ttype
        self.amt = amt
        self.receiver = receiver


class Bank:
    def __init__(self, accounts):
        self.accounts = {k: Account(k, v) for k, v in accounts.items()}
        self.seen_txn = set()
        self.rejected = []

    def validate(self, parts):
        if len(parts) not in (4, 5):
            raise InvalidTransactionError("Malformed record")
        tid, acc, ttype, amt = parts[:4]
        receiver = parts[4] if len(parts) == 5 else None

        if tid in self.seen_txn:
            raise DuplicateTransactionError("Duplicate TXN")
        if acc not in self.accounts:
            raise AccountNotFoundError("Account not found")
        if ttype not in ("deposit", "withdraw", "transfer"):
            raise InvalidTransactionError("Invalid type")
        if amt <= 0:
            raise InvalidTransactionError("Invalid amount")
        if ttype == "transfer" and (not receiver or receiver not in self.accounts):
            raise InvalidTransactionError("Invalid receiver")

        return Transaction(tid, acc, ttype, amt, receiver)

    def apply(self, txn):
        acc = self.accounts[txn.acc]
        if txn.ttype == "deposit":
            acc.balance += txn.amt
        elif txn.ttype == "withdraw":
            if acc.balance < txn.amt:
                raise InsufficientBalanceError("Insufficient balance")
            acc.balance -= txn.amt
        else:
            if acc.balance < txn.amt:
                raise InsufficientBalanceError("Insufficient balance")
            acc.balance -= txn.amt
            self.accounts[txn.receiver].balance += txn.amt

        acc.history.append(txn.__dict__)
        self.seen_txn.add(txn.tid)


bank = Bank(accounts)

total_deposit = 0
total_withdraw = 0
total_transfer = 0

for line in transactions:
    try:
        parts = [p.strip() for p in line.split(",")]
        tid, acc, ttype = parts[0], parts[1], parts[2]
        if len(parts) >= 4:
            amount = float(parts[3])
        else:
            raise InvalidTransactionError("Missing amount")
        parsed_parts = [tid, acc, ttype, amount] + parts[4:]
        txn = bank.validate(parsed_parts)
        bank.apply(txn)
        if txn.ttype == "deposit":
            total_deposit += txn.amt
        if txn.ttype == "withdraw":
            total_withdraw += txn.amt
        if txn.ttype == "transfer":
            total_transfer += txn.amt
    except Exception as e:
        bank.rejected.append((line, str(e)))
    finally:
        pass

sorted_accounts = sorted(bank.accounts.values(), key=lambda a: a.balance, reverse=True)
print("Final balances:", {a.id: a.balance for a in sorted_accounts})
print("Totals:", total_deposit, total_withdraw, total_transfer)
print("Highest:", sorted_accounts[0].id, "Lowest:", sorted_accounts[-1].id)

with open("balances.txt", "w", encoding="utf-8") as f:
    for a in bank.accounts.values():
        f.write(f"{a.id} {a.balance}\n")

with open("rejected.txt", "w", encoding="utf-8") as f:
    for r in bank.rejected:
        f.write(f"{r}\n")

with open("history.json", "w", encoding="utf-8") as f:
    json.dump({a.id: a.history for a in bank.accounts.values()}, f, indent=2)
