marks = {
    "Harry" : 20,
    "Ved" : 15,
    "Carry":2
}

# print(marks.items())
# print(marks.keys())
print(marks.update({"ved": 100, "sakshi":69}))
# print(marks)
# print(marks.get("Ved"))
# print(marks)
# print(marks.values())
# print(marks)
# print(marks.clear())
# print(marks())
value = marks.pop("ved")

print(value)
print(marks)