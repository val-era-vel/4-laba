input_string = input("Введіть рядок: ")
result = ""
for char in input_string:
    if char.isdigit():
        result = result + char
print(result)