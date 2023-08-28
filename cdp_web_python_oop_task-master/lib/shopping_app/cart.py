from ownable import Ownable

class Cart:
    from item_manager import show_items
    def __init__(self, name):
        self.name = name
        self.wallet = Wallet(self)   # UserインスタンスまたはUserを継承したクラスのインスタンスは生成されると、自身をオーナーとするウォレットを持ちます。

    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("Saldo insuficiente en el monedero del propietario del carrito.")
            return

        for item in self.items:
            self.owner.wallet.transfer(self.owner, item.owner, item.price)
            item.transfer_ownership(self.owner)

        self.items = []
        print("Compra exitosa. El carrito ha sido vaciado.")

        print(f"Nuevo saldo del monedero del propietario del carrito: {self.owner.wallet.balance}")
