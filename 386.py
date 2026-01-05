line = input()
zeros = 0
result = ""
for char in line:
    if char == '0':
        zeros += 1
    elif char == '1':
        result += chr(97 + zeros)
        zeros = 0
print(result)

