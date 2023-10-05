from logger import show_data,edit_data,export_data,delete_data
def main():
    my_choice = -1
    file_tel = "tel_f.txt"

# Создает файл если его нет в папке
    with open(file_tel, "a", encoding="utf-8") as file:
        file.write("")

    while my_choice != 0:
        print("Выберите одно из действий:")
        print("1 — Вывести инфо на экран")
        print("2 — Произвести экпорт данных")
        print("3 — Произвести изменение данных")
        print("4 — Произвести удаление данных")
        print("0 — Выход из программы")
        action = int(input("Действие: "))
        if action == 1:
            show_data(file_tel)
        elif action == 2:
            export_data(file_tel)
        elif action == 3:
            edit_data(file_tel)
        elif action == 4:
            delete_data(file_tel)
        else:
            my_choice = 0

    print("До свидания")

if __name__ == "__main__":
    main()