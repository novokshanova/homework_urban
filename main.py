# s = "1"
# b = 1
# b = str(b)
# print(s + b)

def file_operations(filename, text_to_add):

    with open(filename, 'a') as file:

        file.write(text_to_add + '\n')


    with open(filename, 'r') as file:

        content = file.read()
        print("Содержимое файла:\n", content)


    with open(filename, 'r') as file:
        print("Построчное чтение файла:")
        for line in file:
            print(line.strip())