class Products:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def discount(self, percentage):
        self.price = self.price - (self.price * (percentage / 100))

    # Getter
    @property
    def item(self):
        return self._item

    # Setter
    @item.setter
    def item(self, valor):
        self._item = valor.replace("@", "")

    # Getter
    @property
    def price(self):
        return self._price

    # Setter
    @price.setter
    def price(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("$", ""))
        self._price = valor
