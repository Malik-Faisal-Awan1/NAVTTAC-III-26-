# CREATE FILE "testing.py"

def add(a, b):
    return a + b

if __name__ == "__main__":
    # This runs only if testing.py is run directly, not when imported.
    print("Testing testing.py")
    print(add(2, 3))