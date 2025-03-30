class InventoryManager:
    def check_stock(self, product_id):
        # Check product stock
        if product_id:
            return True
        return False

    def reserve_product(self, product_id):
        # Reserve product for the order
        return f"Reserve done for {product_id}"

class PaymentProcessor:
    def process_payment(self, payment_details):
        # Process payment
        return f"Payment done for {payment_details}"

class ShippingCoordinator:
    def arrange_shipping(self, shipping_address):
        # Arrange shipping for the order
        return f"Shipping is arranged for {shipping_address}"

# Facade class
class OrderFacade:
    def __init__(self):
        self.inventory = InventoryManager()
        self.payment = PaymentProcessor()
        self.shipping = ShippingCoordinator()

    def place_order(self, product_id, payment_details, shipping_address):
        if self.inventory.check_stock(product_id):
            print(self.inventory.reserve_product(product_id))
            print(self.payment.process_payment(payment_details))
            print(self.shipping.arrange_shipping(shipping_address))
            print("Order placed successfully.")
        else:
            print("Product is out of stock.")

# Client code
facade = OrderFacade()
facade.place_order(product_id=123, payment_details={'card_number': '1111-2222-3333-4444'}, shipping_address="ABC street")

"""In case of the absence of a facade, the client must directly manage interactions with each subsystem:
Challenges Without Facade:

Increased Complexity: The client must understand the intricacies of each subsystem and manage the interactions, leading to more complex code.
Tight Coupling: Changes in any subsystem's interface or behavior require modifications in the client code, reducing flexibility.
Reduced Maintainability: As the system grows, managing direct interactions with multiple subsystems becomes cumbersome and error-prone.
"""

def place_order2(product_id, payment_details, address):
    # Instantiate subsystem components
    inventory = InventoryManager()
    payment = PaymentProcessor()
    shipping = ShippingCoordinator()

    # Step 1: Check stock
    if not inventory.check_stock(product_id):
        print("Product is out of stock.")
        return

    # Step 2: Reserve product
    print(inventory.reserve_product(product_id))

    # Step 3: Process payment
    if not payment.process_payment(payment_details):
        print("Payment failed.")
    else:
        print(f"Payment done for {payment_details}")

    # Step 4: Arrange shipping
    print(shipping.arrange_shipping(address))

    print("Order placed successfully.")

# Example usage
product_id = 1123
payment_details = {'card_number': '71111-2222-3333-4444'}
address = "Main Street"
place_order2(product_id, payment_details, address)