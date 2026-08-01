# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: FieldNotes
def add_profile_menu():
    profiles = {"Администратор": "admin", "Наблюдатель": "observer", "Гость": "guest"}
    print("\n--- Управление профилями ---")
    print("1) Просмотр профиля")
    print("2) Смена профиля")
    print("3) Создание нового профиля")
    print("4) Выход из приложения")
    choice = input("Выбор: ").strip()

    if choice == "1":
        name = profiles.get(current_profile, "Неизвестный")
        print(f"Текущий профиль: {name}")
        return
    elif choice == "2":
        new_name = input("Введите имя нового профиля: ").strip()
        if new_name in ["Администратор", "Наблюдатель", "Гость"]:
            current_profile = new_name
            print(f"Профиль изменён на: {current_profile}")
        else:
            print("Ошибка: допустимые профили — Администратор, Наблюдатель, Гость")
    elif choice == "3":
        name = input("Имя профиля: ").strip()
        if name in profiles.values():
            print("Это имя уже занято")
        else:
            current_profile = name
            print(f"Профиль '{name}' создан. Текущий: {current_profile}")
    elif choice == "4":
        print("До свидания!")
        return

add_profile_menu()
