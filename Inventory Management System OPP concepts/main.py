class Product:
    def __init__(self, product_id, name, price, quantity):
        self.__product_id = product_id  # encapsulation
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    # Getters and setters for encapsulation
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def set_price(self, new_price):
        self.__price = new_price

    def set_quantity(self, new_quantity):
        self.__quantity = new_quantity

    def update_quantity(self, amount):
        self.__quantity += amount

    # Polymorphism example
    def display_info(self):
        print(f"{self.__name} - Price: {self.__price}, Quantity: {self.__quantity}")

# Derived class: Electronics (inherits Product)
class Electronics(Product):
    def __init__(self, product_id, name, price, quantity, brand, warranty_years):
        super().__init__(product_id, name, price, quantity)
        self.brand = brand
        self.warranty_years = warranty_years

    def display_info(self):  # overridden method
        super().display_info()
        print(f"Brand: {self.brand}, Warranty: {self.warranty_years} years")

# Derived class: Grocery (inherits Product)
class Grocery(Product):
    def __init__(self, product_id, name, price, quantity, expiry_date):
        super().__init__(product_id, name, price, quantity)
        self.expiry_date = expiry_date

    def display_info(self):  # overridden method
        super().display_info()
        print(f"Expiry Date: {self.expiry_date}")

# Inventory class to manage products
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        pid = product.get_product_id()
        if pid in self.products:
            print("Product already exists. Updating quantity...")
            self.products[pid].update_quantity(product.get_quantity())
        else:
            self.products[pid] = product
        print(f"Product '{product.get_name()}' added/updated successfully.")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product {product_id} removed.")
        else:
            print("Product not found.")

    def show_all_products(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            for product in self.products.values():
                product.display_info()
                print("------------") #for spaces

#Example usage
if __name__ == "__main__":
    inventory = Inventory()

    #Adding electronics
    laptop = Electronics(101, "Laptop", 120000, 5, "Dell", 2)
    mobile = Electronics(102, "Smartphone", 80000, 10, "Samsung", 1)

    #Adding groceries
    rice = Grocery(201, "Basmati Rice", 250, 20, "2025-12-31")
    oil = Grocery(202, "Cooking Oil", 500, 15, "2025-09-10")

    #Add to inventory
    inventory.add_product(laptop)
    inventory.add_product(mobile)
    inventory.add_product(rice)
    inventory.add_product(oil)

    print("\nAll Products in Inventory:")
    inventory.show_all_products()