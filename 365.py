text = input("Введіть рядок: ")
result = ""
for char in text:
    if char.isupper() and result != "":
        result = result + " " + char
    else:
        result = result + char
print(result)

