while True:
    try:
        age = int(input("Please enter your age (or 0 to exit): "))

        if age == 0:
            break

        if age < 3:
            ticket_price = 0
        elif age <= 12:
            ticket_price = 15
        else:
            ticket_price = 20

        print(f"The cost of your movie ticket is ${ticket_price}")

    except ValueError:
        print("Invalid input. Please enter a valid age (or 0 to exit).")

print("Thank you for using the ticket pricing system!")
