raw = "name=Fraz; age=23; city=Lahore; role=Student"
pairs = [p.strip() for p in raw.split(";") if p.strip()]

data = {}
for pair in pairs:
    key, value = pair.split("=", 1)   # split only once
    data[key.strip()] = value.strip()

print(data)
# {'name': 'Fraz', 'age': '23', 'city': 'Lahore', 'role': 'Student'}