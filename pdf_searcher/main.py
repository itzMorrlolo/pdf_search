from pypdf import PdfReader
from tkinter import filedialog
def whole_word(data):
    data = data.upper()
    if data == "ДА":
        return True
    elif data == "НЕТ":
        return False
    else:
        print("Данные введены неверно.")
        exit()

print("Выберите pdf файл")
path_to_file = filedialog.askopenfilename()

search_word = input("Введите слово, которое необходимо найти в pdf файле: ")
data_for_whole_word = input("Искать слово целиком? ДА/НЕТ: ")

is_whole_word = whole_word(data_for_whole_word)
reader = PdfReader(path_to_file)
counter = 0
num_page = 0

for page in reader.pages:
    num_page += 1
    text = page.extract_text()
    lines = text.split("\n")
    num_line = 0
    for line in lines:
        if line == "" or line == " ":
            continue

        num_line += 1
        words = line.split()

        if (search_word in words and is_whole_word == True) or (search_word in line and is_whole_word == False):
            counter += 1
            num_word = 0
            for word in words:
                num_word += 1
                if (search_word == word and is_whole_word == True) or (search_word in word and is_whole_word == False):
                    break
            else:
                continue
            print(f"----Слово №{counter}----")
            print(f"страница: {num_page}\nномер строки: {num_line}\nномер слова: {num_word}")

if counter == 0:
    print("Найдено 0 совпадений.")

generate_file_data = input("Хотите сгенерировать текстовый файл с результатами поиска? ДА/НЕТ: ")

if generate_file_data.upper() == "ДА":
    with open("результаты_поиска.txt", "w") as file:
        file.write(f"Результаты поиска семантических единиц по запросу '{search_word}' в файле '{path_to_file}' на странице {num_page}:\n")
        file.write(f"Найдено {counter} семантических единиц.")
    print("Файл с результатами успешно создан.")
else:
    print("Программа завершена без создания текстового файла.")