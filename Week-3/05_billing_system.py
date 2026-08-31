"""Week 3 Mini Project: OOP-based Billing System."""


class Product:
    def __init__(self, name, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity cannot be negative.")
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    @property
    def subtotal(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, tax_rate=0.18):
        if tax_rate < 0:
            raise ValueError("Tax rate cannot be negative.")
        self.tax_rate = float(tax_rate)
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    @property
    def subtotal(self):
        return sum(product.subtotal for product in self.products)

    @property
    def tax(self):
        return self.subtotal * self.tax_rate

    @property
    def total(self):
        return self.subtotal + self.tax

    def display(self):
        print("\n" + "=" * 62)
        print("                         FINAL BILL")
        print("=" * 62)
        print(f"{'Product':<25}{'Price':>10}{'Qty':>7}{'Amount':>15}")
        print("-" * 62)
        for product in self.products:
            print(f"{product.name:<25}₹{product.price:>9.2f}{product.quantity:>7}₹{product.subtotal:>14.2f}")
        print("-" * 62)
        print(f"{'Subtotal':<47}₹{self.subtotal:>14.2f}")
        print(f"{'Tax (' + str(self.tax_rate * 100) + '%)':<47}₹{self.tax:>14.2f}")
        print(f"{'Grand Total':<47}₹{self.total:>14.2f}")
        print("=" * 62)


def main():
    bill = Bill(tax_rate=0.18)
    print("OOP Billing System")
    print("Enter products. Leave product name blank to finish.\n")

    while True:
        name = input("Product name: ").strip()
        if not name:
            break
        try:
            price = float(input("Price: ₹"))
            quantity = int(input("Quantity: "))
            bill.add_product(Product(name, price, quantity))
        except ValueError as error:
            print(f"Invalid input: {error}")

    if bill.products:
        bill.display()
    else:
        print("No products were added.")


if __name__ == "__main__":
    main()
