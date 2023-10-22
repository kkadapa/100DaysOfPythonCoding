class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        self.items.append((product, quantity))

    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

    def view_cart(self):
        print("Your Shopping Cart:")
        for product, quantity in self.items:
            print(f"{product.name} x{quantity}")
        print(f"Total: ${self.calculate_total():.2f}")

def main():
    print("Welcome to the Online Shopping System!")
    cart = ShoppingCart()
    while True:
        print("\nMenu:")
        print("1. Add Product to Cart")
        print("2. View Cart")
        print("3. Checkout")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: $"))
            quantity = int(input("Enter quantity: "))
            product = Product(name, price)
            cart.add_item(product, quantity)
            print(f"{quantity} {name}(s) added to the cart.")

        elif choice == "2":
            cart.view_cart()

        elif choice == "3":
            total = cart.calculate_total()
            print(f"Total cost: ${total:.2f}")
            print("Thank you for shopping with us!")
            break

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
