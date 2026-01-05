text = input("Рядок:")
char_to_find = input("Символ:")
count = 0
index_found = -2
for i in range(len(text)):
    if text[i] == char_to_find:
        count += 1
        if count == 1:
            index_found = -1
        elif count == 2:
            index_found = i
            break
print(index_found)






