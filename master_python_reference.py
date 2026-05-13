"""NAVTTC Advance Python — Master Reference

This single file is a compact, hands-on reference covering core and advanced
Python concepts. Each section is runnable and includes short examples.
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

from typing import List, Dict


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
