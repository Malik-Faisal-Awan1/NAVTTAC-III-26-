import utils

raw = input("Enter full name: ")
print("Clean:", utils.clean_name(raw))

marks = input("Enter marks (0-100): ")
if utils.is_valid_marks(marks):
    print("Marks saved:", marks)
else:
    print("Invalid marks")

print(utils.fraz)