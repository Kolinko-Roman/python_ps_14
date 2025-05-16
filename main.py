import json
import os

# === Завдання 1: Статистика гравця ===
def update_game_stats():
    filename = "game_stats.json"
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            stats = json.load(f)
    else:
        stats = {"games_played": 0, "wins": 0, "losses": 0}

    stats["games_played"] += 1
    result = input("Результат гри (win/lose): ").strip().lower()
    if result == "win":
        stats["wins"] += 1
    elif result == "lose":
        stats["losses"] += 1

    with open(filename, 'w') as f:
        json.dump(stats, f, indent=2)
    print("Оновлена статистика:", stats)

# === Завдання 2: Контакти ===
def manage_contacts():
    filename = "contacts.json"
    contacts = {}

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            contacts = json.load(f)

    while True:
        print("\n[Контакти] 1-Додати  2-Переглянути  3-Вихід")
        choice = input("Ваш вибір: ")
        if choice == "1":
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            contacts[name] = phone
            with open(filename, 'w') as f:
                json.dump(contacts, f, indent=2)
        elif choice == "2":
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        elif choice == "3":
            break

# === Завдання 3: Клієнтська база ===
def manage_clients():
    filename = "clients.json"
    clients = []

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            clients = json.load(f)

    def save():
        with open(filename, 'w') as f:
            json.dump(clients, f, indent=2)

    while True:
        print("\n[Клієнти] 1-Додати 2-Пошук 3-Оновити 4-Видалити 5-Переглянути всі 6-Вихід")
        choice = input("Ваш вибір: ")
        if choice == "1":
            name = input("Ім'я: ")
            email = input("Email: ")
            clients.append({"name": name, "email": email})
            save()
        elif choice == "2":
            key = input("Пошук за іменем: ")
            results = [c for c in clients if key.lower() in c["name"].lower()]
            print("Знайдено:", results)
        elif choice == "3":
            name = input("Ім'я для оновлення: ")
            for c in clients:
                if c["name"] == name:
                    c["email"] = input("Новий email: ")
                    save()
                    break
        elif choice == "4":
            name = input("Ім'я для видалення: ")
            clients = [c for c in clients if c["name"] != name]
            save()
        elif choice == "5":
            for c in clients:
                print(c)
        elif choice == "6":
            break

# === Головне меню ===
def main():
    while True:
        print("\n=== ГОЛОВНЕ МЕНЮ ===")
        print("1. Статистика гри")
        print("2. Контакти")
        print("3. Клієнтська база")
        print("4. Вихід")
        choice = input("Оберіть дію: ")
        if choice == "1":
            update_game_stats()
        elif choice == "2":
            manage_contacts()
        elif choice == "3":
            manage_clients()
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
