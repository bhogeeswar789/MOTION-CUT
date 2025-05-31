import datetime
import time

festivals = {
    "Happy New Year": "01-01-2025",
    "Holi": "13-03-2025",
    "Diwali": "20-10-2025",
    "Christmas": "20-12-2025"
}

def check_reminders():
    today = datetime.date.today()
    for name, date_str in festivals.items():
        try:
            fest_date = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
            days_left = (fest_date - today).days
            if days_left == 0:
                print(f"Today is {name}! Enjoy!")
            elif 0 < days_left <= 7:
                print(f"{name} is in {days_left} day(s) on {fest_date}.")
        except ValueError:
            print(f"Wrong date format for {name}.")

def add_festival():
    name = input("Festival name: ")
    date_str = input("Date (DD-MM-YYYY): ")
    try:
        datetime.datetime.strptime(date_str, "%d-%m-%Y")
        festivals[name] = date_str
        print(f"{name} saved.")
    except ValueError:
        print("Invalid date format.")

def run():
    while True:
        print("\n1. Check reminders")
        print("2. Add festival")
        print("3. View festivals")
        print("4. Exit")
        choice = input("Choose (1-4): ")

        if choice == '1':
            check_reminders()
        elif choice == '2':
            add_festival()
        elif choice == '3':
            for name, date_str in festivals.items():
                print(f"- {name}: {date_str}")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")
        time.sleep(1)

if __name__ == "__main__":
    run()