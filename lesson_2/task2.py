class Shop:

    sales = 0

    def __init__(self, name, items_sold):
        self.name = name
        self.items_sold = items_sold

        Shop.sales += items_sold

    def increase_sales(self, increase):
        self.items_sold += increase
        Shop.sales += increase

    def print_sales():
        print(Shop.sales)
