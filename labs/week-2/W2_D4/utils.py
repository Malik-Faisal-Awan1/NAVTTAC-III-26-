def clean_name(name: str) -> str:
    name = name.strip()
    name = " ".join(name.split())
    return name.title()

def is_valid_marks(m: str) -> bool:
    return m.isdigit() and 0 <= int(m) <= 100

fraz = "Advanced Python Programming"