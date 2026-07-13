# Create a class Laptop with attributes: brand, RAM, price.
# Create 2 objects
# with different values.

class laptop:
    brand = "default",
    RAM = "8gb",
    price = "1 Lakh"

laptop1 = laptop()
laptop1.brand= "Macbook"
laptop1.RAM= "16GB"
print("Laptop1 Brand - ", laptop1.brand)

laptop2= laptop()
laptop2.brand= "Lenovo"
print("Laptop2 Brand - ", laptop2.brand)
print(laptop2.price)