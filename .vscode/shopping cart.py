# shopping cart
menu = {
    "apple": 10,
    "banana": 20,
    "carrot": 30,
    "watch": 300,
    "tissue paper": 200,
}


def start_shopping():
    cart = {}
    total_price = 0

    print("--- MENU ---")
    for item, price in menu.items():
        print(f"{item.capitalize()}: ${price}")
    print("----------------")

    while True:
        selection = input("\nEnter item to buy (or 'quit' to finish): ").lower()

        if selection == "quit":
            break


        if selection in menu:
            try:
                quantity = int(input(f"How many {selection}s do you want? "))
                if quantity > 0:
                    cart[selection] = cart.get(selection, 0) + quantity
                else:
                    print("Quantity must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a number for quantity.")
        else:
            print("Sorry, that item is not in stock.")

    print("\n--------- YOUR RECEIPT ---------")
    for item, qty in cart.items():
        subtotal = menu[item] * qty
        total_price += subtotal
        print(f"{item.capitalize()} x{qty}: ${subtotal}")

    print(f"\nTOTAL PRICE: ${total_price}")
    print("--- THANK YOU FOR SHOPPING ---")


start_shopping()