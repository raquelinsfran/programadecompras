class Item:
    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.owner = owner
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    def transfer_ownership(self, new_owner):
        self.owner = new_owner  # Cambia el propietario del artículo al nuevo propietario

    @staticmethod
    def item_all():
        return Item.instances
