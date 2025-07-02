def split_bill():
    try:
        total_amount = float(input("Total bill amount (₹): "))
        tip = input("Tip percentage (press Enter to skip): ")
        if tip:
            total_amount += total_amount * (float(tip) / 100)

        num_people = int(input("Number of people: "))
        if num_people <= 0:
            print("People count must be more than 0.")
            return

        people = []
        for i in range(num_people):
            name = input(f"Name of person {i+1}: ")
            people.append(name)

        share = round(total_amount / num_people, 2)

        print("\n--- Split Summary ---")
        for name in people:
            print(f"{name} pays: ₹{share}")

        print(f"\nTotal: ₹{round(total_amount, 2)}")

    except ValueError:
        print("Invalid input. Use numbers only.")

split_bill()
